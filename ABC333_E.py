import io
import sys
import pdb
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations, accumulate
from heapq import heappush, heappop
sys.setrecursionlimit(10**6)
from bisect import bisect_right, bisect_left
from math import gcd
import math

_INPUT = """\
6
13
1 2
1 3
1 1
1 3
1 2
2 3
1 3
1 3
2 3
1 3
2 2
2 3
2 1
4
2 3
1 4
2 1
1 2
30
1 25
1 2
1 10
1 18
2 18
1 11
2 11
1 21
1 6
2 2
2 10
1 11
1 24
1 11
1 3
1 2
1 18
2 25
1 8
1 10
1 11
2 18
2 10
1 10
2 2
1 24
1 10
2 10
1 25
2 6
"""

def solve(test):
  N=int(input())
  q=[list(map(int, input().split())) for _ in range(N)]
  tmp=[deque() for _ in range(N)]
  ans=[-1]*N
  for i in reversed(range(N)):
    t,x=q[i]
    x-=1
    if t==1:
      if len(tmp[x])>0:
        y=tmp[x].pop()
        ans[i]=1
      else:
        ans[i]=0
    else:
      tmp[x].append(i)
  if sum(len(tmp[i]) for i in range(N))>0:
    print(-1)
  else:
    k=0
    now=0
    for i in range(N):
      if ans[i]==1:
        now+=1
      elif ans[i]==-1:
        now-=1
      k=max(k,now)
    print(k)
    print(*[ans[i] for i in range(N) if ans[i]!=-1])

def random_input():
  from random import randint,shuffle
  N=randint(1,10)
  M=randint(1,N)
  A=list(range(1,M+1))+[randint(1,M) for _ in range(N-M)]
  shuffle(A)
  return (" ".join(map(str, [N,M]))+"\n"+" ".join(map(str, A))+"\n")*3

def simple_solve():
  return []

def main(test):
  if test==0:
    solve(0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0)
  else:
    for i in range(1000):
      sys.stdin = io.StringIO(random_input())
      x=solve(1)
      y=simple_solve()
      if x!=y:
        print(i,x,y)
        print(*[line for line in sys.stdin],sep='')
        break

#0:提出用、1:与えられたテスト用、2:ストレステスト用
main(0)
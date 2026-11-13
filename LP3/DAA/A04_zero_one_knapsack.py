"""SPPU Group A #4: correct dynamic programming and TRUE branch and bound."""
from dataclasses import dataclass
import heapq
import itertools

def knapsack_dp(items, capacity):
    """Items are (positive integer weight, nonnegative value). Returns max value, chosen indexes."""
    if capacity<0 or any(int(w)!=w or w<=0 or v<0 for w,v in items):raise ValueError('Invalid integer weights/value/capacity')
    n=len(items);dp=[[0]*(capacity+1) for _ in range(n+1)]
    for i,(weight,value) in enumerate(items,1):
        for c in range(capacity+1):
            dp[i][c]=dp[i-1][c]
            if weight<=c:dp[i][c]=max(dp[i][c],dp[i-1][c-weight]+value)
    c=capacity;chosen=[]
    for i in range(n,0,-1):
        w,v=items[i-1]
        if w<=c and dp[i][c] != dp[i-1][c]:chosen.append(i-1);c-=w
    return dp[n][capacity],list(reversed(chosen))

def knapsack_branch_and_bound(items, capacity):
    """Exact best-first B&B, fractional upper bound; not ratio-greedy."""
    if capacity<0 or any(w<=0 or v<0 for w,v in items):raise ValueError('Invalid input')
    ranked=sorted(((w,v,idx) for idx,(w,v) in enumerate(items)),key=lambda z:z[1]/z[0],reverse=True)
    n=len(ranked)
    def bound(level,weight,value):
        if weight>capacity:return float('-inf')
        best=value;remaining=capacity-weight
        for w,v,_ in ranked[level:]:
            if remaining<=0:break
            take=min(1.,remaining/w);best+=v*take;remaining-=w*take
        return best
    counter=itertools.count();best=0;best_taken=()
    heap=[(-bound(0,0,0),next(counter),0,0,0,())]
    while heap:
        neg_upper,_,level,weight,value,taken=heapq.heappop(heap)
        if -neg_upper < best-1e-10:continue
        if level==n:
            if value>best:best=value;best_taken=taken
            continue
        w,v,idx=ranked[level]
        if weight+w<=capacity:
            nv=value+v
            if nv>best:best=nv;best_taken=taken+(idx,)
            ub=bound(level+1,weight+w,nv)
            if ub>=best-1e-10:heapq.heappush(heap,(-ub,next(counter),level+1,weight+w,nv,taken+(idx,)))
        ub=bound(level+1,weight,value)
        if ub>=best-1e-10:heapq.heappush(heap,(-ub,next(counter),level+1,weight,value,taken))
    return best,sorted(best_taken)

if __name__=='__main__':
    items=[(10,60),(20,100),(30,120)];capacity=50
    print('DP:',knapsack_dp(items,capacity));print('Branch and bound:',knapsack_branch_and_bound(items,capacity))
    assert knapsack_dp(items,capacity)[0]==knapsack_branch_and_bound(items,capacity)[0]==220
    print('DP O(n*capacity) time/space; B&B exponential worst case with fractional upper bound')

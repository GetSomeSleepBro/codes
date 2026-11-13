"""SPPU Group A #3: fractional knapsack by greedy value/weight ratio."""
import argparse

def fractional_knapsack(items,capacity):
    if capacity<0:raise ValueError('Negative capacity')
    if any(w<=0 or v<0 for w,v in items):raise ValueError('Require positive weights and nonnegative values')
    remaining=capacity;value=0.;chosen=[]
    for i,(w,v) in sorted(enumerate(items),key=lambda x:x[1][1]/x[1][0],reverse=True):
        if remaining<=0:break
        fraction=min(1.,remaining/w);chosen.append((i,fraction));value+=fraction*v;remaining-=fraction*w
    return value,chosen
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--capacity',type=float,default=50);args=ap.parse_args()
    items=[(10,60),(20,100),(30,120)]
    print('Items (weight,value):',items,'capacity:',args.capacity)
    print('Maximum value, (zero-based item, fraction):',fractional_knapsack(items,args.capacity))
    print('Time O(n log n); auxiliary space O(n)')

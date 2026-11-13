"""SPPU Group A #6: deterministic vs randomized quicksort, instrument comparisons."""
import random,time,argparse

def quicksort(data,randomized=False,seed=42):
    values=list(data);rnd=random.Random(seed);metrics={'comparisons':0,'partitions':0}
    def sort(lo,hi):
        if lo>=hi:return
        pivot_pos=rnd.randint(lo,hi) if randomized else hi
        values[hi],values[pivot_pos]=values[pivot_pos],values[hi]
        pivot=values[hi];i=lo
        for j in range(lo,hi):
            metrics['comparisons']+=1
            if values[j]<=pivot:values[i],values[j]=values[j],values[i];i+=1
        values[i],values[hi]=values[hi],values[i];metrics['partitions']+=1
        # Smaller segment first, loop on the larger segment avoids deep call stack.
        if i-lo<hi-i:
            sort(lo,i-1);sort(i+1,hi)
        else:
            sort(i+1,hi);sort(lo,i-1)
    sort(0,len(values)-1)
    return values,metrics

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=150);args=ap.parse_args()
    if args.n>900:ap.error('Use <=900 elements for comparative lab demonstration')
    data=list(range(args.n))
    for randomized in [False,True]:
        t=time.perf_counter();out,stats=quicksort(data,randomized);elapsed=time.perf_counter()-t
        assert out==sorted(data)
        print(('Randomized' if randomized else 'Deterministic'),stats,'seconds',round(elapsed,6))
    print('Average O(n log n), worst O(n^2); randomized expected O(n log n)')

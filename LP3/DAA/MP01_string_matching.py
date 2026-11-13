"""SPPU Group A mini-project #9: Naive vs Rabin-Karp exact string matching."""
from time import perf_counter
import argparse

def naive(text,pattern):
    if not pattern:return list(range(len(text)+1))
    return [i for i in range(len(text)-len(pattern)+1) if text[i:i+len(pattern)]==pattern]

def rabin_karp(text,pattern,base=256,prime=1000000007):
    n,m=len(text),len(pattern)
    if not m:return list(range(n+1))
    if m>n:return []
    power=pow(base,m-1,prime);hp=0;ht=0
    for i in range(m):hp=(hp*base+ord(pattern[i]))%prime;ht=(ht*base+ord(text[i]))%prime
    found=[]
    for i in range(n-m+1):
        if hp==ht and text[i:i+m]==pattern:found.append(i)  # collision checked
        if i<n-m:ht=((ht-ord(text[i])*power)*base+ord(text[i+m]))%prime
    return found

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--text',default='ABABDABACDABABCABAB');p.add_argument('--pattern',default='ABAB');args=p.parse_args()
    for func in (naive,rabin_karp):
        t=perf_counter();matches=func(args.text,args.pattern)
        print(func.__name__,matches,'elapsed',round(perf_counter()-t,7),'s')
    assert naive(args.text,args.pattern)==rabin_karp(args.text,args.pattern)
    print('Naive O(n*m) worst; Rabin-Karp expected O(n+m), O(n*m) collision worst')

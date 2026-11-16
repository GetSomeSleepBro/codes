"""SPPU Group A #2: deterministic prefix-free Huffman coding."""
from collections import Counter
import heapq
import itertools
import argparse

def huffman_codes(text: str) -> dict[str,str]:
    if not text: return {}
    seq=itertools.count();heap=[]
    for ch,freq in sorted(Counter(text).items()):
        heapq.heappush(heap,(freq,next(seq),ch))
    if len(heap)==1: return {text[0]:'0'}
    while len(heap)>1:
        f1,_,left=heapq.heappop(heap);f2,_,right=heapq.heappop(heap)
        heapq.heappush(heap,(f1+f2,next(seq),(left,right)))
    codes={}
    def walk(node,prefix):
        if isinstance(node,str): codes[node]=prefix;return
        walk(node[0],prefix+'0');walk(node[1],prefix+'1')
    walk(heap[0][2],'')
    return codes

def encode(text,codes): return ''.join(codes[c] for c in text)

def decode(bits,codes):
    reverse={v:k for k,v in codes.items()};result=[];cur=''
    for b in bits:
        if b not in '01': raise ValueError('Only bits allowed')
        cur+=b
        if cur in reverse:result.append(reverse[cur]);cur=''
    if cur:raise ValueError('Incomplete codeword')
    return ''.join(result)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--text',default='aaaabccddddde');args=p.parse_args()
    codes=huffman_codes(args.text);bits=encode(args.text,codes)
    print('Codes:',codes,'Encoded:',bits,'Decoded:',decode(bits,codes))
    assert decode(bits,codes)==args.text
    print('Greedy heap complexity: O(k log k + n) for k symbols and n input chars')

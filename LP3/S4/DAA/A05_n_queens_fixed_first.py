"""SPPU Group A #5: N queens with a designated first queen (row 0, first_col)."""
import argparse

def n_queens(n,first_col=0):
    if n<1 or not 0<=first_col<n:raise ValueError('Use n>=1 and 0<=first_col<n')
    pos=[first_col];cols={first_col};diag1={-first_col};diag2={first_col}
    def solve(row):
        if row==n:return True
        for col in range(n):
            if col in cols or row-col in diag1 or row+col in diag2:continue
            cols.add(col);diag1.add(row-col);diag2.add(row+col);pos.append(col)
            if solve(row+1):return True
            pos.pop();cols.remove(col);diag1.remove(row-col);diag2.remove(row+col)
        return False
    return pos.copy() if solve(1) else None

def show(pos):
    n=len(pos);return '\n'.join(' '.join('Q' if c==pos[r] else '.' for c in range(n)) for r in range(n))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=4);ap.add_argument('--first-col',type=int,default=1);args=ap.parse_args()
    result=n_queens(args.n,args.first_col)
    print('No solution with this fixed queen' if result is None else show(result))
    print('Backtracking, worst-case exponential (upper bound O(n!))')

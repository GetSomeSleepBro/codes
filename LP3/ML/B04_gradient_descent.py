"""SPPU Group B #4: gradient descent for f(x)=(x+3)^2 from x=2."""
import argparse

def f(x):return (x+3)**2
def gradient(x):return 2*(x+3)
def gradient_descent(start=2.,learning_rate=.1,max_iterations=200,tolerance=1e-7):
    if not 0<learning_rate<1:raise ValueError('For this quadratic choose 0<learning_rate<1')
    x=float(start);history=[x]
    for _ in range(max_iterations):
        next_x=x-learning_rate*gradient(x);history.append(next_x)
        if abs(next_x-x)<tolerance:break
        x=next_x
    return history[-1], f(history[-1]),history
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--rate',type=float,default=.1);p.add_argument('--quick',action='store_true',help='Accepted for consistency; this script already runs quickly');args=p.parse_args()
    x,y,h=gradient_descent(learning_rate=args.rate)
    print(f'Local minimum x={x:.8f}, y={y:.12f}, steps={len(h)-1}')
    assert abs(x+3)<1e-4

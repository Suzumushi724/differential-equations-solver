import numpy as np
import matplotlib.pyplot as plt
from diffeq_solver import DiffEquSolver

def dxdt(t,x):
    ret = 2*t
    return ret

def answer(t):
    return t**2+1

def main():
    x0 = 1
    t = 0
    h = 0.01
    N = 1000

    solver = DiffEquSolver(t,h,N,(x0,),dxdt)
    result1 = solver.euler()
    result2 = solver.fixed_euler()
    result3 = solver.runge()
    
    T = np.arange(t,N*h,h)
    ans = answer(T)
    
    print("Euler method:"+str(np.var(result1[:,0]-ans))+"\r\n"
         +"Fixed-Euler method:"+str(np.var(result2[:,0]-ans))+"\r\n"
         +"Runge–Kutta method:"+str(np.var(result3[:,0]-ans)))
    
    fig,ax = plt.subplots()
    ax.plot(T,result1[:,0],marker='v',markevery=30,label="euler")
    ax.plot(T,result2[:,0],marker='^',markevery=30,label="fixed_euler")
    ax.plot(T,result3[:,0],marker='x',markevery=30,label="runge")
    ax.plot(T,ans,marker='o',markevery=30,label="answer")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
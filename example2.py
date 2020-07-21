import numpy as np
import matplotlib.pyplot as plt
from diffeq_solver import DiffEquSolver

def dxdt(t,x):
    k = 1 
    m = 0.1 
    w = np.sqrt(k/m)
    w0 = w 
    f = 1 
    return np.array([x[1],-1*w**2 * x[0] + f/m*np.cos(w0*t)])

def answer(t):
    k = 1 
    m = 0.1 
    w = np.sqrt(k/m)
    w0 = w 
    f = 1
    return np.cos(w*t)+f/(2*w*m)*t*np.sin(w*t)

def main():
    x0 = 1
    v0 = 0
    t = 0
    h = 0.01
    N = 1000

    solver = DiffEquSolver(t,h,N,(x0,v0),dxdt)
    result1 = solver.euler()
    result2 = solver.fixed_euler()
    result3 = solver.runge()
    
    T = np.arange(t,N*h,h)
    ans = answer(T)
    
    print('Euler method:'+str(np.var(result1[:,0]-ans))+'\r\n'
         +'Fixed-Euler method:'+str(np.var(result2[:,0]-ans))+'\r\n'
         +'Runge–Kutta method:'+str(np.var(result3[:,0]-ans)))
    
    fig,ax = plt.subplots()
    ax.plot(T,result1[:,0],marker='v',markevery=30,label='Euler')
    ax.plot(T,result2[:,0],marker='^',markevery=30,label='Fixed_Euler')
    ax.plot(T,result3[:,0],marker='x',markevery=30,label='Runge-Kutta')
    ax.plot(T,ans,marker='o',markevery=30,label='Answer')
    plt.xlabel('t')
    plt.ylabel('x')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
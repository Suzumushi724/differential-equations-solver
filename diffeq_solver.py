import numpy as np
from copy import copy

class DiffEquSolver:
    
    def __init__(self,t,h,N,init,func):
        self.t = t
        self.h = h
        self.N = N
        self.init = init
        self.x = np.array(list(init),dtype=np.float)
        self.func = func
    
    #Euler method
    def euler(self):
        t = self.t
        h = self.h
        x = copy(self.x)
        func = self.func
        X = np.zeros((self.N,len(self.init)))
        for i in range(self.N):
            k = func(t,x)*h
            x += k
            t += h
            X[i] = x
        return X

    #Fixed-Euler method
    def fixed_euler(self):
        t = self.t
        h = self.h
        x = copy(self.x)
        func = self.func
        X = np.zeros((self.N,len(self.init)))
        for i in range(self.N):
            k = (func(t,x) + func(t+h,x+h*func(t,x)))*h/2
            x += k
            t += h
            X[i] = x
        return X

    #Runge–Kutta method
    def runge(self):
        t = self.t
        h = self.h
        x = copy(self.x)
        func = self.func
        X = np.zeros((self.N,len(self.init)))
        for i in range(self.N):
            k1 = func(t,x)
            k2 = func(t+h/2, x+k1*h/2)
            k3 = func(t+h/2, x+k2*h/2)
            k4 = func(t+h, x+k3*h)
            x += h/6*(k1 + 2*k2 + 2*k3 + k4)
            t += h
            X[i] = x
        return X
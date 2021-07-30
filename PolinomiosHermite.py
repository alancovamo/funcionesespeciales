# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 02:13:49 2021

@author: Alan
"""
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x=Symbol('x')
n=10

def H(n):
    if n==0:
        dx=x-x+1
        return dx
    else:
        
        f = exp((-x**2)/2)
        
        for i in range(n):
            
            dx=f.diff(x)
            f=dx
        return dx*((-1)**n)*exp((x**2/2))


print('el polinomio de Hermite de orden %i es %s' %(n,H(n)))
    

X=np.linspace(-10,10,1000)
Z=X-X
plt.figure(0)

plt.xlim(-3,4)
plt.ylim(-10,20)
#plt.gca().set_aspect('equal', adjustable='box')
plt.plot(X,Z,label='orden 0')
#plt.figure(figsize=(10,7))

for i in range(n):
    y=lambdify(x, H(i+1))
    

    plt.plot(X,y(X),label='orden %d' %(i+1))
    plt.legend(loc='lower right')

    
  
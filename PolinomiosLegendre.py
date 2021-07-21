# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 13:13:12 2021

@author: Alan
"""
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

x=Symbol('x')

n=6


def g(n):
    
    if n==0:
        dx=x-x
        return dx
    else:
    
        f =(1/(factorial(n)*2**n) )*(x**2-1)**n
    
        for i in range(n):
        
            dx=f.diff(x)
        
            f=dx
    
        return dx 



print('el polinomio de Legendre de orden %d es %s' %(n,g(n)))

X=np.linspace(-1,1,100)
Z=X-X
plt.figure(0)

plt.xlim(-1,1)
plt.ylim(-1,1)
#plt.gca().set_aspect('equal', adjustable='box')
plt.plot(X,Z,label='orden 0')

for i in range(n):
    y=lambdify(x, g(i+1))
    

    plt.plot(X,y(X),label='orden %d' %(i+1))
    plt.legend(loc='lower right')






#print(y(1))
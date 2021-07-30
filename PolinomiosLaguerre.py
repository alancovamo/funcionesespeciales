# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 20:39:22 2021

@author: Alan
"""
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
x=Symbol('x')



k=0
n=5

def L(n,k):
    if n==0:
        return 1
    else:
        a=1/(factorial(n))*(x**-k)*exp(x)
        f= (x**(n+k))*exp(-x)
        for i in range(n):
            dx=f.diff(x)
            f=dx
        return dx*a

z=np.linspace(-5,10,1000)

Z=z-z
plt.figure(0)
plt.plot(z,Z)
plt.ylim(-10,20)
for i in range(n):
    y=lambdify(x,L(i+1,k))
    plt.plot(z,y(z))

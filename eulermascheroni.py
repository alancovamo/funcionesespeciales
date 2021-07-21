# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 22:25:43 2021

@author: Alan
"""
from timeit import default_timer


import numpy as np
    
def eu1(n):
    k=0
    j=0
    for i in range(0,int(n/4)):
        k=k+(1/(i+1))
    for i in range(int(n/4),int(n/2)):
        j=j+(1/(i+1))
    for i in range(int(n/2),int(3*n/4)):
        l=l+(1/(i+1))
    for i in range(int(3*n/4),n):
        m=m+(1/(i+1))
    return (k+j+l+m)-np.log(n)    

print(eu1(int(1e11)))

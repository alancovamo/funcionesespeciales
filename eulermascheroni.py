# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 22:25:43 2021

@author: Alan
"""
from timeit import default_timer
from numba import vectorize
import numpy as np
import math

@vectorize
def cpu_eu(n):
    k=0
    for i in range(0,int(n)):
        k=k+(1/(i+1))
    return k-np.log(n)    
 



n=1e10    

print(cpu_eu(n))



%%timeit cpu_eu(n)

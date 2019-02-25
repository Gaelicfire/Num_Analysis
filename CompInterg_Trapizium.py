# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:15:57 2019

@author: Gealicfire

Composite Trapezium Rule:

Inputs: f(x) = function to intergated 
        a = lower bound to intergrate over
        b = upper bound ''               ''
        e = Error control, so the approx will be within 'e' of the true value

Outputs: I = Aprrox intergrand based on composite trapezium rule with N 
             divisons.        
"""

import numpy as np
import matplotlib.pyplot as plt
import math

#Inputs
def f(x):
    return 1/(np.exp(x)*x)
a=1 #range to intergrate on
b=2
e=1/10**5 #accuracy to which we want to approximate intergrand

#Useful variables
N=1000 #number of points to approx derive 
K=(b-a)/(N) #distance between x_j+1 and x_j 
x=np.arange(a-K,b+2*K,K) #points to derive

#Function to be Intergrated
y = f(x) 

#Finite difference for second derivative
F2 = np.zeros((N+2))
for i in range(N):
    F2[i+1] = (y[i+2] - 2*y[i+1] + y[i])/(K**2) 
M = np.amax(F2) #maximise derivative over the range

#Composite Trapizium rule error 
N= (1/(((12*e)/(M*(b-a))))**(1/2)) + 1
N = math.ceil(N)


#Useful Variables
h=(b-a)/(N)   #Distance between points
I=0 
x=np.arange(a,b+h,h)
y = f(x)

#Composite Trapezium Rule
for i in range(N-1):
    I = y[i+1] + I
I = (h/2)*(y[0] + y[N]) + h*I 
  
print(I) 
print(N)

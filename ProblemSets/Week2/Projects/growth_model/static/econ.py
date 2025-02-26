#======================================================================
# 
#     sets the economic functions for the "Growth Model", i.e., 
#     the production function, the utility function
#     
#
#     Simon Scheidegger, 11/16 ; 07/17
#====================================================================== 

from parameters import *
import numpy as np
import os

method = os.environ["Method"]
#====================================================================== 
#utility function u(c,l) 

def utility(cons=[], lab=[]):
    sum_util=0.0
    n=len(cons)
    for i in range(n):
        nom1=(cons[i]/big_A)**(1.0-gamma) -1.0
        den1=1.0-gamma
        
        nom2=(1.0-psi)*((lab[i]**(1.0+eta)) -1.0)
        den2=1.0+eta
        
        sum_util+=(nom1/den1 - nom2/den2)
    
    util=sum_util
    
    return util 


#====================================================================== 
# output_f 

def output_f(kap=[], lab=[]):
    if 'static' == method:
        fun_val = big_A*(kap**psi)*(lab**(1.0 - psi))
        return fun_val
    else:
        return stochastic_output_f(kap,lab)

def stochastic_output_f(kap=[], lab=[]):
    theta_index = np.random.randint(5, size=1)[0]
    theta = 0.9+theta_index*0.05
    fun_val = theta*big_A*(kap**psi)*(lab**(1.0 - psi))
    return fun_val



#======================================================================

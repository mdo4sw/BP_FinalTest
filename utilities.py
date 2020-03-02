# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:07:12 2020

@author: mdo
"""

import time
import timeit

from configobj import ConfigObj
import numpy as np 
from numpy import linalg

import os
import matplotlib.pyplot as plt
from pylab import figure, savefig
from matplotlib.patches import Rectangle
from os.path import join

class utilities:
    def __init__(self):
        self.stepTime = 3
        self.output_dir=""
        
    def get_setupInfo(self, setupInfoFile):
        return ConfigObj(setupInfoFile)
    
    def cross(self,x1,x2):
        return x1*x2
    
    def square(self,x):
        return np.square(x)
    
    def cube(self,x):
        return np.power(x,3)
    
    def leastSquare(self,x_vstack,y):
        return linalg.lstsq(x_vstack,y,rcond=None)[0]
        
    def transpose(self,x):
        return np.transpose(x)
    
    
## This is the most updated version of the code 
## updated at 17/12 17:35

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation 

class Particle():
    
    def __init__(self, id=0, position = np.zeros(2),velocity = np.zeros(2), radius = 1E-2 , mass =1):
        self.id = id
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.mass = mass

class sim():

    X = 2
    Y = 2

    def __init__(self, dt = 1E-2, dN = 10):
        self.dt = dt
        self.dN = dN
    
    def particles(self):




    
## This is the most updated version of the code 
## updated at 17/12 17:35

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

##
from matplotlib.animation import FuncAnimation
##

class Particle():
    
    def __init__(self, id=0, position = np.zeros(2),velocity = np.zeros(2), radius = 1E-2 , mass =1, colour = "blue"):
        self.id = id
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.mass = mass
        self.colour = colour 

class sim():

    X = 2
    Y = 2

    def __init__(self, dt = 1E-2, Num = 10):
        self.dt = dt
        self.Num = Num
        ##
        self.particles =  [Particle(i) for i in range(0,Num)]
        ##
    
    def collision_dection(self):
        print("Hello World")

    def increment(self):
        self.collision_dection()
        for i in self.particles:
            i += i.position + i.velocity*self.dt

    def particle_position(self):
        return [ i for i in self.particles]








    
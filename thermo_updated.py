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
        return [ i.position for i in self.particles]

    def particle_colour(self):
        return [ i.colour for i in self.particles]


sim = sim()

decided_v = 1000

## Set the position and velocity of the particles 
for particle in sim.particle:
    particle.position = np.random.uniform([-sim.X/2,-sim.Y/2], [sim.X/2,sim.Y/2], size =2) 
    particle.velocity = np.random.uniform([-decided_v,-decided_v], [decided_v,decided_v], size =2)
##

    

## plot code 

fig, ax = plt.subplots()

scatter = ax.scatter([],[])

def init():
    ax.set_xlim(-sim.X/2, sim.X/2)
    ax.set_ylim(-sim.Y/2, sim.Y/2)
    return scatter, 

def update(frame):
    sim.increment()
    scatter.set_offsets(np.array(sim.particle_positions()))
    return scatter, 

ani = FuncAnimation(fig, update, frame=range(1200), init_func = init, blit = True, interval = 1/30, repeat = True)

plt.show()









    
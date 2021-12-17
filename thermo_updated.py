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

    # The boundaries of the box should be much bigger than the particles(at least 100 times)
    X = 1
    Y = 1

    def __init__(self, dt = 1E-5, Num = 500):
        self.dt = dt
        self.Num = Num
        ##
        self.particles =  [Particle(i) for i in range(0,Num)]
        ##
    
    def collision_dection(self):
        
        ##detect if the particles collide with the wall 
        ignore_list = [] ##adding ignore_list to ensure we haven't double counted the colliding particles
        for particle in self.particles:
            
            x,y = particle.position
            if(self.X/2< x+particle.radius) or (-self.X/2> x-particle.radius):
                particle.velocity[0] *=-1
            if(self.Y/2< y+particle.radius) or (-self.Y/2> y-particle.radius):
                particle.velocity[1] *=-1

            id1 = particle.id
            v1 = particle.velocity
            m1 = particle.mass
            p1 = particle.position
  
            ## Make use of ignore list   
            if (particle in ignore_list):
                continue

        ## Check if the particles collide with other particle 
            for particle2 in self.particles:

                v2 = particle2.velocity
                m2 = particle2.mass
                p2 = particle2.position

                if(id1 == particle2.id):
                    continue

                elif np.dot(p1-p2,p1-p2) <= (particle.radius+particle2.radius)**2:
                    # Formula from Wikipeida 
                    particle.velocity = v1 - 2*m1/(m1+m2)* np.dot(v1-v2,p1-p2)/np.dot(p1-p2,p1-p2)*(p1-p2)
                    particle2.velocity = v2 - 2*m2/(m1+m2)* np.dot(v2-v1,p2-p1)/np.dot(p2-p1,p2-p1)*(p2-p1)
                    ignore_list.append(particle2)


    def increment(self):
        self.collision_dection()
        # To simulate that the particles is moving 
        for i in self.particles:
            i.position += i.velocity*self.dt

    def particle_position(self):
        return [i.position for i in self.particles]

    def particle_colour(self):
        return [i.colour for i in self.particles]


sim = sim()

decided_v = 10000
## Set the position and velocity of the particles 
for particle in sim.particles:
    particle.position = np.random.uniform([-sim.X/2,-sim.Y/2], [sim.X/2,sim.Y/2], size =2) 
    particle.velocity = np.random.uniform([-decided_v,-decided_v], [decided_v,decided_v],size=2) 
##

## Set id 0 particles to be blue
sim.particles[0].colour = "red"

## plot code 
fig, ax = plt.subplots()

scatter = ax.scatter([],[])

def init():
    ax.set_xlim(-sim.X/2, sim.X/2)
    ax.set_ylim(-sim.Y/2, sim.Y/2)
    return scatter, 

def update(frame):
    sim.increment()
    scatter.set_offsets(np.array(sim.particle_position()))
    scatter.set_color(np.array(sim.particle_colour()))
    return scatter, 
                
ani = FuncAnimation(fig, update, frames=range(500),init_func = init, blit = True, interval = 100, repeat = False)
#
#

#frames = how many frames do you want to use 
#init_func = the first frame you wanna display (optional)
#blit = True -> only draw the changing data again -> display each frame faster 
#interval = how long will one frame last (in milliseconds)
#repeat = False -> don't repeat after all the frames has been played 
 
plt.show()


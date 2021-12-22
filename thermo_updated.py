## This is the most updated version of the code 

## some features to implemented afterwards
## 1. intermolecular force 
## 2. when the particle collide, changes their colour
## 3. modify the x-axis of histogram

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

##
from matplotlib.animation import FuncAnimation
##

##Some useful constants
K_B = 1.380649*10**(-23)
velocity_of_O_mole = np.sqrt(481**2/2)
mass_of_O_mole = 5.31*10**(-26)

class Particle():
    
    def __init__(self, id=0, position = np.zeros(2),velocity = np.zeros(2), radius = 1E-2 , mass=1, colour = "blue"):
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

    def __init__(self, dt = 1E-8, Num = 10):
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

    def particle_speed(self):
        return [np.sqrt(np.dot(i.velocity,i.velocity)) for i in self.particles]

    ##here assume all the particles have the same mass
    def particle_mass(self):
        mass = self.particles[0].mass
        return mass

    def temperature(self):
        Total_KE = 0 
        for i in self.particles:
            Total_KE += 0.5*i.mass*np.dot(i.velocity,i.velocity)
        return (Total_KE/self.Num)*(2/3)/(K_B)

#set sim variables 
Np = 100

velocity = np.sqrt(700**2/2)
sim = sim(Num = Np,dt = 1E-4)
## Set the position,velocity and mass of the particles 
for particle in sim.particles:
    particle.position = np.random.uniform([-sim.X/2+0.01,-sim.Y/2+0.01], [sim.X/2-0.01,sim.Y/2-0.01], size =2) 
    particle.velocity = np.array([velocity,velocity]) 
    particle.mass = mass_of_O_mole
##

## Set id 0 particles to be red
sim.particles[0].colour = "red"

## plot code 
fig, (ax,ax2) = plt.subplots(figsize=(5,9), nrows = 2)


ax.set_aspect("equal")
vs = np.linspace(0,1000,25)
n_avg = 50
freqs_matrix = np.tile((np.histogram(sim.particle_speed(), bins = vs))[0].astype(np.float64),(n_avg,1))

scatter = ax.scatter([],[])
## The first list is for setting x-values
## The second list is for setting y-values

##Create bar chart 
bar = ax2.bar(vs,[0]*len(vs),width=0.9*np.gradient(vs), align="edge", alpha = 0.8)

##Create the theoretical prediction
dv = 100
range1 = np.arange(0,1200)

## The terms dv*Np
## dv exists=> trapzedioal sim
## Np exists=> f(v) is the probability density function, times Np means how many particles can we found in that velocity 
mass1 = sim.particle_mass()
T =sim.temperature()
theo = ax2.plot(range1, dv*Np*(mass1/(2*np.pi*K_B*T))**(3/2)*4*np.pi*range1**2*np.exp(-(mass1*range1**2)/(2*K_B*T)))

def init():
    ax.set_xlim(-sim.X/2, sim.X/2) # set the range for x axis animation
    ax.set_ylim(-sim.Y/2, sim.Y/2) # set the range for y axis animation

    ax2.set_xlim(vs[0],vs[-1]) # set the range for x axis bar-chart
    ax2.set_ylim(0,Np) # set the range for y axis bar-chart
    ax2.set(xlabel = "Particle speed", ylabel="Number of particles")
    return (scatter, *bar.patches)


def update(frame):
    sim.increment()

    freqs, bins = np.histogram(sim.particle_speed(), bins = vs)
    freqs_matrix[frame%n_avg] = freqs
    freqs_mean = np.mean(freqs_matrix,axis=0) 
    freqs_max = np.max(freqs_matrix) 

    for rect, height in zip(bar.patches, freqs_mean):
        rect.set_height(height)

    ## Create temperature mark
    T_txt = ax.text(sim.X/3.5,ax.get_ylim()[1]*0.8,s="") # set the x-y position of the temperature show
    T_txt.set_text(f"{sim.temperature():.2f} K")
    
    if np.abs(freqs_max - ax2.get_ylim()[1])>5:
        ax2.set_ylim(0,freqs_max)
        fig.canvas.draw()

    scatter.set_offsets(np.array(sim.particle_position())) ##update the data (position of particles) to the plane
    scatter.set_color(np.array(sim.particle_colour())) ##update the data (colour of particles) to the plane


    return (scatter,*bar.patches,T_txt)
                
ani = FuncAnimation(fig, update, frames=range(1200),init_func = init, blit = True, interval = 100, repeat = False)
#fig -> place to display the animation
#update = func to call each time to update the animation

#frames = how many frames do you want to use 
#init_func = the first frame you wanna display (optional)
#blit = True -> only draw the changing data again -> display each frame faster 
#interval = how long will one frame last (in milliseconds)
#repeat = False -> don't repeat after all the frames has been played 
 
plt.show()

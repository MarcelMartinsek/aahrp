from matplotlib.markers import MarkerStyle
import numpy as np
from functions import *
from matplotlib import pyplot as plt
from matplotlib.animation import *

class Particle: 
    def __init__(self,fname):
        self.bounds = bounds_arrays[fname]
        self.par = np.random.uniform(low=self.bounds[:,0],high=self.bounds[:,1],size=len(self.bounds))
        self.value = function[fname](self.par)
        self.vel = np.random.uniform(low=-0.5,high=0.5,size=len(self.bounds))
        self.pbest = self.par
        self.pbest_val = self.value
    
    def __repr__(self):
        # return '{' + self.par + ' (' + self.pbest + ')' + '}'
        return '{' + self.par + '}'

    def move(self, w, c1, c2, gbest, f):
        r1 = np.random.uniform(0,1,size=len(self.bounds))
        r2 = np.random.uniform(0,1,size=len(self.bounds))
        # print(r1,r2,self.vel,self.pbest-self.par,sep = "    |    ")
        self.vel = w*self.vel + c1*r1*(self.pbest-self.par) + c2*r2*(gbest-self.par)
        newpar = self.par + self.vel
        #use bisection if the particle would move out of bounds(lower velocity by half)
        while ~((self.bounds[:,0] <= newpar.T).all() and (newpar.T <= self.bounds[:,1]).all()):
            self.vel /= 2
            newpar = self.par + self.vel
        self.par = newpar
        
        self.value = f(self.par)
        if self.value < self.pbest_val:
            self.pbest = self.par
            self.pbest_val = self.value

        return self.value,self.par
        #TODO UPDATE GBEST AFTER RETURN

    def __eq__(self, __o: object) -> bool:
        return self.value == __o.value

    def __lt__(self, __o: object) -> bool:
        return self.value < __o.value
        
    def approx(self, __o: object,tol=10e-12) -> bool:
        # print((self.value-tol),__o.value,(self.value+tol))
        return (self.value-tol) <= __o.value <= (self.value+tol)

    def checkbounds(self):
        pass

    

class ParticleSwarm:
    def init_pop(self):
        swarm = []
        
        return swarm

    def __init__(self, fname, pop_size=50,max_iter=100,w_limits=[0.9,0.4],c1=1,c2=1,N=10):
        self.obj_fun_name = fname
        self.obj_fun = function[fname]
        self.bounds = bounds_arrays[fname]
        self.pop_size = pop_size
        self.max_iter = max_iter
        self.w_limits = w_limits
        self.c1 = c1
        self.c2 = c2
        self.value = None
        self.par = None
        self.swarm = []
        for i in range(self.pop_size):
            self.swarm.append(Particle(self.obj_fun_name))
        self.swarm.sort(key=lambda p:p.pbest_val)
        self.history = [[p.par for p in self.swarm]]
        self.stop_check_N = N

    def optimize(self,tol=10e-10):
        objective = self.obj_fun
        swarm = self.swarm

        gbest = swarm[0]

        stop_condition = False
        iter = self.max_iter
        w = self.w_limits[0]
        w_delta = (self.w_limits[0] - self.w_limits[1])/(iter-1)
        # print(self.w_limits,w_delta)
        c1 = self.c1
        c2 = self.c2
        topN = swarm[0:self.stop_check_N]
        while((not stop_condition) and iter>0):
            hist = []
            # print(iter)
            for i,p in enumerate(swarm):
                # print(i)
                # print("vel is: ",vel[i,:])
                val,par = p.move(w, c1, c2, gbest.par, objective)
                hist.append(par)
                if val < gbest.value:
                    gbest = p
            self.history.append(hist)

            swarm.sort(key=lambda x:x.value)
            # print(w)
            w -= w_delta
            # stop_condition = topN == swarm[0:10]
            stop_condition = all([topN[i].approx(swarm[i],tol) for i in range(self.stop_check_N)])
            iter -= 1
        if(iter==0):
            print("Did not converge before max_iter iterrations.")
            
        self.swarm = swarm
        return gbest
    
fname = "Schaffer1"
ps = ParticleSwarm(fname,max_iter=1000,w_limits=[0.5,0.001],c1=0.3,c2=0.5,N=10)
gbest = ps.optimize(tol = 10e-8)


fig = plt.figure()
ax = plt.axes(xlim=ps.bounds[0], ylim=ps.bounds[1])
line, = ax.plot([], [], 'ro',markersize=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    line.set_data([p[0] for p in ps.history[i]],[p[1] for p in ps.history[i]])
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=len(ps.history), interval=20)


f = r"./test.gif" 
writergif = PillowWriter(fps=30) 
# anim.save(f, writer=writergif)
plt.show()
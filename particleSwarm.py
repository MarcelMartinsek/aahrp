import numpy as np
from functions import *
class ParticleSwarm:
    def __init__(self, fname, pop_size=50,max_iter=100,w_limits=[0.9,0.4],c1=1,c2=1):
        self.obj_fun = function[fname]
        self.bounds = bounds_arrays[fname]
        self.pop_size = pop_size
        self.max_iter = max_iter
        self.w_limits = w_limits
        self.c1 = c1
        self.c2 = c2
        self.value = None
        self.par = None

    def init_swarm(self):
        swarm = np.random.uniform(low=bounds[:,0],high=bounds[:,1],size=(self.pop_size,len(self.bounds)))
        return swarm

    def optimize(self):
        bounds = self.bounds
        objective = self.obj_fun

        # swarm = self.init_swarm(len(par),bounds)
        swarm = np.random.uniform(low=bounds[:,0],high=bounds[:,1],size=(self.pop_size,len(self.bounds)))
        pbest = np.copy(swarm)
        pbest_value = [self.obj_fun(p) for p in pbest]
        gbest_ix = np.argmin(pbest_value)
        #initialize particle velocities to small amounts
        vel = np.random.uniform(low=-0.5,high=0.5,size=(self.pop_size,len(self.bounds)))


        stop_condition = False
        iter = self.max_iter
        w = self.w_limits[0]
        w_delta = (self.w_limits[0] - self.w_limits[1])/(iter-1)
        print(self.w_limits,w_delta)
        c1 = self.c1
        c2 = self.c2

        history = [swarm]
        while(~stop_condition and iter>0):
            for i in range(self.pop_size):
                r1 = np.random.uniform(0,0.5,size=len(bounds))
                r2 = np.random.uniform(0,0.5,size=len(bounds))
                vel[i,:] = w*vel[i] + c1*r1*(pbest[i]-swarm[i]) + c2*r2*(pbest[gbest_ix]-swarm[i])
                # print("vel is: ",vel[i,:])
                swarm[i,:] += vel[i,:]

                fitness = objective(swarm[i,:])
                if fitness < pbest_value[i]:
                    pbest_value[i] = fitness
                    pbest[i] = swarm[i]
                    if fitness < pbest_value[gbest_ix]:
                        gbest_ix = i
            print(w)
            w -= w_delta
            history.append(np.copy(swarm))
            iter -= 1
        return history,pbest_value

fname = "Schaffer1"
ps = ParticleSwarm(fname)
history,pbest_value = ps.optimize()
bounds = bounds_arrays[fname]
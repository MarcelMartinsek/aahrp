import numpy as np
from functions import *
class ParticleSwarm:
    def __init__(self, fname, pop_size=50,w_limits=[0.9,0.4],c1=1,c2=1):
        self.obj_fun = function[fname]
        self.bounds = bounds[fname]
        self.pop_size = pop_size
        self.w_limits = w_limits
        self.c1 = c1
        self.c2 = c2
        self.value = None
        self.par = None

    def init_swarm(self):
        swarm = np.random.uniform(low=bounds[:,0],high=bounds[:,1],size=(self.pop_size,len(self.bounds)))
        return swarm

    def optimize(self, par, bounds):
        # swarm = self.init_swarm(len(par),bounds)
        swarm = np.random.uniform(low=bounds[:,0],high=bounds[:,1],size=(self.pop_size,len(self.bounds)))
        pbest = np.copy(swarm)
        pbest_value = [self.obj_fun(p) for p in pbest]
        gbest_ix = np.argmin(pbest_value)[0]
        vel = np.random.uniform(low=bounds[:,0],high=bounds[:,1],size=(self.pop_size,len(self.bounds)))
        return swarm,pbest_value

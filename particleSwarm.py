import numpy as np

class ParticleSwarm:
    def __init__(self, function, pop=50,w_limits=[0.9,0.4],c1=1,c2=1):
        self.obj_fun = function
        self.population = pop
        self.w_limits = w_limits
        self.c1 = c1
        self.c2 = c2

    def init_swarm(self,dim,bounds):
        swarm = np.random.uniform(low=bounds[:,0],high=bounds[:,1],size=(self.population,dim))
        return swarm

    def optimize(self, par, bounds):
        swarm = self.init_swarm(len(par),bounds)
        pbest = np.copy(swarm)
        pbest_value = [self.obj_fun(p) for p in pbest]

        return swarm,pbest_value

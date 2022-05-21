import numpy as np
from functions import *

class SimulatedAnnealing:
    def __init__(self, fname, temperature=100, iterations=10, alpha=0.95, stop=5):
        self.f = function[fname]
        self.bounds = bounds_arrays[fname]
        self.T = temperature
        self.it = iterations
        self.alpha = alpha
        self.stop = stop

    def optimize(self):
        par_current = np.random.uniform(low=self.bounds[:, 0], high=self.bounds[:, 1], size=len(self.bounds))
        val_current = self.f(par_current)
        par_minimal = np.copy(par_current)
        val_minimal = val_current
        prev_min_val = 0
        i = 0
        s = 0 # stagnating tracker
        while s < self.stop and i < self.it:
            i = i + 1
            s = s + 1
            T = self.T
            while T > 0.1:
                T = T * self.alpha
                k = 0
                while k < 10:
                    k = k + 1
                    par = np.zeros(len(self.bounds))
                    par_candidate = np.zeros(len(self.bounds))
                    val_candidate = 0
                    #generate 2 random candidates and take best one
                    for u in range(2):
                        for j in range(len(self.bounds)):
                            ne = par_current[j] + 10 * np.random.normal(0)
                            while ne < self.bounds[0, 0] or ne > self.bounds[0, 1]:
                                ne = par_current[j] + 10 * np.random.normal(0)
                            par[j] = ne
                        val = self.f(par)
                        if u == 0:
                            par_candidate = np.copy(par)
                            val_candidate = val
                        elif val < val_candidate:
                            par_candidate = np.copy(par)
                            val_candidate = val
                    print(val_minimal)
                    if val_candidate < val_minimal:
                        par_minimal = np.copy(par_candidate)
                        val_minimal = val_candidate
                    if val_candidate < val_current:
                        par_current = np.copy(par_candidate)
                        val_current = val_candidate
                    else:
                        p = np.exp(-(val_candidate - val_current) / T)
                        if np.random.random() < p:
                            par_current = np.copy(par_candidate)
                            val_current = val_candidate
            if prev_min_val == val_minimal:
                s = s + 1
            else:
                s = 0
            prev_min_val = val_minimal
        return val_minimal, par_minimal

fname = "Schaffer1"
ps = SimulatedAnnealing(fname, temperature=1000, alpha=0.95, iterations=3, stop=3)
opt = ps.optimize()
print(opt,np.abs(optimums[fname]-opt[0]))

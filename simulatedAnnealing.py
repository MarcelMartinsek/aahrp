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
        prev_par = np.random.uniform(low=self.bounds[:, 0], high=self.bounds[:, 1], size=len(self.bounds))
        prev_val = self.f(prev_par)
        min_par = prev_par
        min_val = prev_val
        prev_min_val = 0
        i = 0
        s = 0
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
                    curr_par = np.zeros(len(self.bounds))
                    curr_val = 0
                    for u in range(2):
                        for j in range(len(self.bounds)):
                            ne = prev_par[j] + 10 * np.random.normal(0)
                            while ne < self.bounds[0, 0] or ne > self.bounds[0, 1]:
                                ne = prev_par[j] + 10 * np.random.normal(0)
                            par[j] = ne
                        val = self.f(par)
                        if u == 0:
                            curr_par = np.copy(par)
                            curr_val = val
                        elif val < curr_val:
                            curr_par = np.copy(par)
                            curr_val = val
                    print(min_val)
                    if curr_val < min_val:
                        min_par = np.copy(curr_par)
                        min_val = curr_val
                    if curr_val < prev_val:
                        prev_par = np.copy(curr_par)
                        prev_val = curr_val
                    else:
                        p = np.exp(-(curr_val - prev_val) / T)
                        if np.random.random() < p:
                            prev_par = np.copy(curr_par)
                            prev_val = curr_val
            if prev_min_val == min_val:
                s = s + 1
            else:
                s = s + 1
            prev_min_val = min_val
        return min_val, min_par

fname = "Schaffer1"
ps = SimulatedAnnealing(fname, temperature=1000, alpha=0.95, iterations=3, stop=3)
opt = ps.optimize()
print(opt)

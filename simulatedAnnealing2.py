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
        T = self.T
        history = [par_current]
        while s < self.stop and i < self.it:
            i = i + 1
            s = s + 1
            T = T * self.alpha
            if(T<0.1):
                print("Temp RESET")
                T = self.T
            k = 0
            while k < 10:
                # print(k,end=",")
                k = k + 1
                par = np.zeros(len(self.bounds))
                par_candidate = np.zeros(len(self.bounds))
                val_candidate = 0
                #generate 2 random candidates and take best one
                for u in range(2):
                    for j in range(len(self.bounds)):
                        par = par_current + 5*np.random.uniform(low=[-1],high=[1],size=len(par))
                        while ~((self.bounds[:,0] <= par).all() and (par <= self.bounds[:,1]).all()):
                            par = par_current + np.random.uniform(low=[-1],high=[1],size=len(par))

                    val = self.f(par)
                    if u == 0:
                        par_candidate = np.copy(par)
                        val_candidate = val
                    elif val < val_candidate:
                        par_candidate = np.copy(par)
                        val_candidate = val
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
                print(val_minimal,s)
                s = 0
            prev_min_val = val_minimal
            history.append(par_current)

        if(i==self.it):
            print("Max iterations reached")
        if(s==self.stop):
            print("Stagnation reached")
        return val_minimal, par_minimal,history

# fname = "Schaffer1"
# ps = SimulatedAnnealing(fname, temperature=500, alpha=0.95, iterations=100, stop=30)
# opt = ps.optimize()
# print(opt[0:2],np.abs(optimums[fname]-opt[0]))

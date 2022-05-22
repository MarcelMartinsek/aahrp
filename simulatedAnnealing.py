import numpy as np
from functions import *

class SimulatedAnnealing:
    def __init__(self, fname, temperature=1000, iterations=100, stop=10, n_coeff=1, grad=1, e=1, h=0.1):
        self.f = function[fname]
        self.bounds = bounds_arrays[fname]
        self.T = temperature
        self.it = iterations
        self.stop = stop
        self.n_coeff = n_coeff
        self.grad = grad
        self.e = e
        self.h = h

    def gradientMethod(self, x0, e=1, h=0.1, tol=0.001, maxit=100000):
        call = 0
        x = np.copy(x0)
        for i in range(maxit):
            grad = np.zeros(len(x0))
            for j in range(len(x0)):
                x0_new = np.copy(x0)
                x0_new[j] = x0_new[j] + e
                if x0_new[j] < self.bounds[j, 0] or x0_new[j] > self.bounds[j, 1]:
                    grad[j] = 0
                    break
                grad[j] = (self.f(x0_new) - self.f(x0)) / e
                call = call + 2
            x = x0 - (h * grad)
            if (x[0]-x0[0] < tol) and (x[1]-x0[1] < tol):
                break
            x0 = np.copy(x)
        v = self.f(x)
        call = call + 1
        return v, x, call

    def optimize(self):
        call = 0
        par_current = np.random.uniform(low=self.bounds[:, 0], high=self.bounds[:, 1], size=len(self.bounds))
        val_current = self.f(par_current)
        call = call + 1
        par_opt = np.copy(par_current)
        val_opt = val_current
        prev_min_val = 0
        i = 0
        s = 0  # stagnating tracker
        T = self.T
        history = [par_current]
        while s < self.stop and i < self.it:
            i = i + 1
            s = s + 1
            T = T * 0.95
            if(T<0.1):
                # print("Temp RESET")
                T = self.T
            k = 0
            while k < 10:
                # print(k,end=",")
                k = k + 1
                par = np.zeros(len(self.bounds))
                par_candidate = np.zeros(len(self.bounds))
                val_candidate = 0
                # generate 10 random candidates and take the best one
                for u in range(10):
                    for j in range(len(self.bounds)):
                        par = par_current + self.n_coeff * np.random.uniform(low=[-1], high=[1],size=len(par))
                        while ~((self.bounds[:, 0] <= par).all() and (par <= self.bounds[:, 1]).all()):
                            par = par_current + self.n_coeff * np.random.uniform(low=[-1], high=[1], size=len(par))
                    val = self.f(par)
                    call = call + 1
                    if u == 0:
                        par_candidate = np.copy(par)
                        val_candidate = val
                    elif val < val_candidate:
                        par_candidate = np.copy(par)
                        val_candidate = val
                if val_candidate < val_opt:
                    par_opt = np.copy(par_candidate)
                    val_opt = val_candidate
                if val_candidate < val_current:
                    par_current = np.copy(par_candidate)
                    val_current = val_candidate
                else:
                    p = np.exp(-(val_candidate - val_current) / T)
                    if np.random.random() < p:
                        par_current = np.copy(par_candidate)
                        val_current = val_candidate
            if prev_min_val == val_opt:
                s = s + 1
            else:
                # print(val_opt, s)
                s = 0
            prev_min_val = val_opt
            history.append(par_current)
        # if i == self.it:
        #     print("Max iterations reached.")
        # if s == self.stop:
        #     print("Stagnation reached.")
        if self.grad == 1:
            val_opt, par_opt, call_grad = self.gradientMethod(par_opt, e=self.e, h=self.h)
            call = call + call_grad
        return val_opt, par_opt, history, call


# temperature, iterations, stop, n_coeff, e, h
parameters = {
    "Schaffer1": [200, 1000, 30, 5, 1.5, 0.01],
    "Schaffer2": [500, 100, 30, 5, 1, 0.3],
    "Salomon": [10, 1000, 100, 1],
    "Griewank": [100, 500, 50, 3, 0.7, 1],
    "PriceTransistor": [1000, 1000, 30, 3],
    "Expo": [1000, 1000, 100, 5, 0.1, 1],
    "Modlangerman": [100, 1000, 50, 3],
    "EMichalewicz": [10, 100, 30, 1],
    "Shekelfox5": [1000, 100, 10, 1],
    "Schwefel": [1000, 100, 10, 2, 8, 0.5]
}

fname = "Griewank"
runs = 1
val_best = 0
par_best = 0
val_avg = 0
par_avg = 0
for i in range(runs):
    pars = parameters[fname]
    if len(pars) == 6:
        ps = SimulatedAnnealing(fname, temperature=pars[0], iterations=pars[1], stop=pars[2], e=pars[3], h=pars[4])
    else:
        ps = SimulatedAnnealing(fname, temperature=pars[0], iterations=pars[1], stop=pars[2], grad=0)
    val_opt, par_opt, history, calls = ps.optimize()
    val_avg = val_avg + val_opt
    par_avg = par_avg + par_opt
    if i == 0:
        par_best = np.copy(par_opt)
        val_best = val_opt
    elif val_opt < val_best:
        par_best = np.copy(par_opt)
        val_best = val_opt
print("Calls of objective function: ", calls)
print("Average: ", val_avg / runs, ", ", par_avg / runs)
print("Best: ", val_best, ", ", par_best)

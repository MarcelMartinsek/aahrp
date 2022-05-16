import numpy as np

bounds = {
	"Schaffer1":       [[-120, 100], [-120, 100]],
	"Schaffer2":       [[-120, 100], [-120, 100]],
	"Salomon":         [[-120, 100], [-120, 100], [-120, 100], [-120, 100], [-120, 100]],
	"Griewank":        [[-550, 500], [-550, 500], [-550, 500], [-550, 500], [-550, 500], [-550, 500], [-550, 500], [-550, 500], [-550, 500], [-550, 500]],
	"PriceTransistor": [[0, 10], [0, 10], [0, 10], [0, 10], [0, 10], [0, 10], [0, 10], [0, 10], [0, 10]],
	"Expo":            [[-12, 10], [-12, 10], [-12, 10], [-12, 10], [-12, 10], [-12, 10], [-12, 10], [-12, 10], [-12, 10], [-12, 10]],
	"Modlangerman":    [[0, 10], [0, 10], [0, 10], [0, 10], [0, 10], [0, 10], [0, 10], [0, 10], [0, 10], [0, 10]],
	"EMichalewicz":    [[0, np.pi], [0, np.pi], [0, np.pi], [0, np.pi], [0, np.pi]],
	"Shekelfox5":      [[0, 10], [0, 10], [0, 10], [0, 10], [0, 10]],
	"Schwefel":        [[-500, 500], [-500, 500], [-500, 500], [-500, 500], [-500, 500], [-500, 500], [-500, 500], [-500, 500], [-500, 500], [-500, 500]],
}

def schaffer1(par):    
    pass

def schaffer2(par) :
    if len(par) != 2 :
        print("WARNING: Schaffer2 works on 2d")
    x = par[0]
    y = par[1]
    prod1 = np.power(x*x+y*y, 0.25)
    prod2 = np.power(50*(x*x+y*y), 0.1)
    return prod1 * (np.sin(np.sin(prod2)) + 1)

def salomon(par):    
    if len(par) != 5 :
        print("WARNING:   Parameter vector should be length 5")
    sum = np.sqrt(np.dot(par,par))
    sum = -np.cos(2*np.pi*sum) + 0.1*sum + 1
    return sum

def griewank(par):    
    pass

def priceTransistor(par):    
    if len(par) != 9 :
        print("WARNING:   Parameter vector should be length 9")
    sumsqr = 0.0
    g = np.array([[0.485, 0.752, 0.869, 0.982],
        [0.369, 1.254, 0.703, 1.455],
        [5.2095, 10.0677, 22.9274, 20.2153],
        [23.3037, 101.779, 111.461, 191.267],
        [28.5132, 111.8467, 134.3884, 211.4823]])
    for k in range(4):
        alpha = (1.0-par[0]*par[1])*par[2]*(np.exp(par[4]*(g[0][k]-0.001*g[2][k]*par[6]-0.001*par[7]*g[4][k]))-1.0) - g[4][k] + g[3][k]*par[1]
        beta = (1.0-par[0]*par[1])*par[3]*(np.exp(par[5]*(g[0][k]-g[1][k]-0.001*g[2][k]*par[6]+g[3][k]*0.001*par[8]))-1.0) - g[4][k]*par[0] + g[3][k]
        sumsqr += alpha*alpha + beta*beta
    sum = par[0]*par[2] - par[1]*par[3]
    sum *= sum
    return sum + sumsqr

def expo(par):    
    pass

def modlangerman(par):    
    pass

def eMichalewicz(par):    
    pass

def shekelfox5(par):    
    pass

def schwefel(par):    
    pass




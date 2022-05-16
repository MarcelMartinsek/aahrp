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

print(salomon((1,1)))
from simulatedAnnealing2 import *
from functions import *
from matplotlib import pyplot as plt
from matplotlib.animation import *
from matplotlib import animation
fname = "Schaffer1"
ps = SimulatedAnnealing(fname, temperature=10, alpha=0.99, iterations=1000, stop=50)
opt = ps.optimize()
history = opt[2]
print(opt[0:2], np.abs(optimums[fname]-opt[0]))
bounds = bounds_arrays[fname]



# X, Y = np.meshgrid(xs, ys)
# Z = np.zeros_like(X)#np.array([function[fname]() for i in row for i in )
# for i,y in enumerate(ys):
#     for j,x in enumerate(xs):
#         Z[i,j] = function[fname]((x,y))
# print(Z)
# # First set up the figure, the axis, and the plot element we want to animate
# fig = plt.figure()
# ax = plt.axes(xlim=bounds[0], ylim=bounds[1])
# plt.contour(X, Y, Z, colors='black')
# plt.show()
fig = plt.figure()
ax = plt.axes(xlim=bounds[0], ylim=bounds[1])
line, = ax.plot([], [], 'ro')

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    line.set_data(history[i][0],history[i][1])
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=len(history), interval=20)


f = r"./testLOCAL.gif" 
writergif = animation.PillowWriter(fps=30) 
anim.save(f, writer=writergif)
plt.show()
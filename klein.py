from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

def surf(u,v):
  X = (3+(1+np.sin(v)) + 2*(1 - np.cos(v)/2)*np.cos(u))*np.cos(v)
  Y = (4+2*(1 - np.cos(v)/2) * np.cos(u))*np.sin(v)
  Z = -2*(1-np.cos(v)/2)*np.sin(u)
  return X,Y,Z

a,b=np.meshgrid(np.linspace(0, 2*np.pi, 20),np.linspace(0, 2*np.pi, 20))
x,y,z = surf(a,b)

fig=plt.figure()
ax=fig.gca(projection="3d")

plot=ax.plot_surface(x,y,z, rstride=1, cstride=1, cmap=cm.jet,linewidth=0, antialiased=False)
plt.show()



from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

def plot(f,g,mu):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = np.arange(10,100,2)
    Y = np.arange(10,100,2)
    X, Y = np.meshgrid(X, Y)
    xlst=X.tolist()[0]
    ylst=Y.tolist()[0]
    l=[]
    for i in range(len(xlst)):
        l.append([xlst[i],ylst[i]])
    Z =[np.array(f(l[i]))+mu*np.array(g(l[i])) for i in range(len(xlst))]
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    ax.set_zlim(-5,5)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()
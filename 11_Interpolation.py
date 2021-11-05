import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = np.linspace(0,10,10)
y = x ** 2

f = interp1d(x, y, kind="linear")

new_x = np.linspace(0,10,30)
result = f(new_x)

plt.scatter(x,y, c='g')
plt.scatter(new_x, result, c='r')
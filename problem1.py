import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

l2 = 75
l3 = 170
y2_to_4 = 45


def f(theta):
    theta_rad = np.radians(theta)
    o23_y = l2 * np.sin(theta_rad)
    x2_to_3 = l2 * np.cos(theta_rad)
    y3_to_4 = o23_y - y2_to_4
    x3_to_4 = np.sqrt(l3 ** 2 - y3_to_4 ** 2)
    return x3_to_4 - x2_to_3


x = np.linspace(0, 360, 100)

plt.plot(x, f(x) - f(0), color='red')

plt.title("Problem 1")
plt.xlabel("Angle (deg)")
plt.ylabel("Horizontal Stroke (mm)")

plt.show()

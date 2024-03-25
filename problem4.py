import numpy as np
from matplotlib import pyplot as plt
import utils


l1 = np.sqrt(47.5 ** 2 + (76 - 12) ** 2)
l2 = 14.0
l3 = 80.0
l4 = 51.26
theta2 = np.degrees(np.arctan2(76 - 12, 47.5))


def f(theta):
    angles = 180.0 - np.degrees(utils.vector_loop(l1, l2, l3, l4, np.radians(180.0 - theta2 - theta))) % 360 - theta2
    return np.vstack([angles[0], utils.get_transmission_angle(angles[1], angles[0])]).T


utils.plot(f, title="Problem 4", xlabel="Angle (deg)", ylabel="Angle (deg)", colors=['red', 'blue'],
           labels=['theta_4', 'mu'])
plt.legend()
plt.show()

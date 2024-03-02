import numpy as np
from matplotlib import pyplot as plt
import utils


def f(theta):
    l1 = 2.22
    l2 = 1.0
    l3 = 2.06
    l4 = 2.33
    theta2 = 26.5
    bap = 31
    ap = 3.06
    angles = np.degrees(utils.vector_loop(l1, l2, l3, l4, np.radians(theta2 - theta))) % 360 - theta2
    theta_p = bap - angles[1]
    a = utils.polar_to_euclidean(l2, theta)
    p_from_a = utils.polar_to_euclidean(ap, theta_p)
    return a + p_from_a


utils.plot(f, title="Problem 2", xlabel="Angle (deg)", ylabel="Position of P", colors=['red', 'blue'],
           labels=['x', 'y'])

plt.legend()
plt.show()

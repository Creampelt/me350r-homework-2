import matplotlib.pyplot as plt
import numpy as np
import utils

l1 = 2.22
l2 = 0.86
l3 = 1.85
l4 = 0.86


def f(theta):
    angles = np.degrees(utils.vector_loop(l1, l2, l3, l4, np.radians(theta))) % 360
    return angles.T


def g(theta):
    bap = 0
    ap = 1.33
    print(np.degrees(utils.find_toggle(l1, l2, l3, l4)))
    angles = np.degrees(utils.vector_loop(l1, l2, l3, l4, np.radians(theta))) % 360
    theta_p = bap - angles[1]
    a = utils.polar_to_euclidean(l2, theta)
    p_from_a = utils.polar_to_euclidean(ap, theta_p)
    return a + p_from_a


plt.subplot(211)
utils.plot(f, title="Problem 3: Joint Angles", xlabel="Angle (deg)", ylabel="Angle (deg)", colors=['purple', 'green'],
           labels=['theta_3', 'theta_4'])
plt.legend()
plt.subplot(212)
utils.plot(g, title="Problem 3: Position of P", xlabel="Angle (deg)", ylabel="Position of P", colors=['red', 'blue'],
           labels=['x', 'y'])
plt.legend()
plt.tight_layout(pad=2.0)
plt.show()

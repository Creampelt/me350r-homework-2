import numpy as np
from matplotlib import pyplot as plt


def find_toggle(l1, l2, l3, l4):
    ac = np.arccos((l2 ** 2 + l1 ** 2 - l3 ** 2 - l4 ** 2) / (2 * l2 * l1))
    added = l3 * l4 / (l2 * l1)
    return np.array([ac + added, ac - added])


def quadratic(a, b, c):
    return (-b - np.sqrt(b ** 2 - 4 * a * c)) / (2 * a)


def vector_loop(l1, l2, l3, l4, theta2):
    c2 = np.cos(theta2)
    s2 = np.sin(theta2)
    k1 = l1 / l2
    k2 = l1 / l4
    k3 = (l2 ** 2 - l3 ** 2 + l4 ** 2 + l1 ** 2) / (2 * l2 * l4)
    k4 = l1 / l3
    k5 = (l4 ** 2 - l1 ** 2 - l2 ** 2 - l3 ** 2) / (2 * l2 * l3)
    a = -k1 - k2 * c2 + k3 + c2
    b = -2 * s2
    c = k1 - k2 * c2 + k3 - c2
    d = c2 - k1 + k4 * c2 + k5
    e = -2 * s2
    f = k1 + (k4 - 1) * c2 + k5
    answers = np.array([quadratic(a, b, c), quadratic(d, e, f)])
    return 2 * np.arctan(answers)


def polar_to_euclidean(r, theta):
    return r * np.vstack([np.cos(np.radians(theta)), np.sin(np.radians(theta))]).T


def get_transmission_angle(theta3, theta4):
    theta_trans = np.abs(theta3 - theta4) % 360
    return np.minimum(theta_trans, 180 - theta_trans)


def plot(f, xmin=0, xmax=360, xstep=360, title='', xlabel='', ylabel='', labels=None, colors=None):
    if labels is None:
        labels = []
    if colors is None:
        colors = []

    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    x = np.linspace(xmin, xmax, xstep)
    plots = f(x)

    try:
        _, n_cols = plots.shape
        for i in range(0, n_cols):
            label = labels[i] if len(labels) > i else ''
            color = colors[i] if len(colors) > i else 'red'
            plt.plot(x, plots[:, i], color=color, label=label)
    except:
        plt.plot(x, plots, color='red')

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

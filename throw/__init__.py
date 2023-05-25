import math


def throw_trajectory(v0, h, a, t, g=10.0):
    x = v0 * math.cos(a) * t
    return x, -0.5 * g / (((v0 * math.cos(a) ** 2)) * x**2 + math.tan(a) * x + h)

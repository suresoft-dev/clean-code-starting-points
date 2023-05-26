from dataclasses import dataclass
import math


def calculate_x_velocity(velocity, angle):
    return velocity * math.cos(angle)


@dataclass
class Throw:
    velocity: float
    height: float
    angle: float


def throw_trajectory(throw: Throw, time, gravity=9.81):
    velocity_x = calculate_x_velocity(throw.velocity, throw.angle)
    x = velocity_x * time
    y = vertical_position(throw, gravity, x)
    return x, y


def vertical_position(throw: Throw, gravity, x):
    numerator = -0.5 * gravity
    angle_velocity = math.tan(throw.angle)
    velocity_x = calculate_x_velocity(throw.velocity, throw.angle)
    denominator = quadratic_function(velocity_x**2, angle_velocity, throw.height, x)
    y = numerator / denominator
    return y


def quadratic_function(a, b, c, x):
    return a * x**2 + b * x + c

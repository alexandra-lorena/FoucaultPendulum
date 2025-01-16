import numpy as np
from scipy.ndimage import minimum
from scipy.integrate import odeint


# Constants
L = 30 #Length of pendulum in meters
g = 9.81 #Gravitational acceleration, m/s^2
omega = 7.27e-5 #Angular velocity of Earth, rad/s
phi = np.radians(45) #φ,Latitude of pendulum

# Initial conditions
a_0 = np.radians(10)
b_0 = np.radians(0)
x_0 = 0.1
y_0 = 0.1
initial_conditions = [a_0, b_0, x_0, y_0]

# Time interval
start_time = 0
end_time = 1000
time_values = np.arange(start = start_time, stop = end_time, step = 0.01)


# Solving ODE
def solve_ode(ode, initial_conditions, time_values, index):
    solution = odeint(func = ode, y0 = initial_conditions, t = time_values)
    return solution.T[index]

def ode(initial_conditions, t):
    a, b, x, y = initial_conditions
    da, db = x, y
    dx = (np.sin(a) * np.cos(a) * y**2 + 2 * omega * np.sin(a) * (np.cos(phi) * np.sin(a) * np.cos(b) + np.sin(phi) * np.cos(a)) * y
         - (g/L) * np.sin(a))
    dy = ((-2 * np.cos(a) * x * y - 2 * omega * (np.cos(phi) * np.sin(a) * np.cos(b) + np.sin(phi) * np.cos(a)) * x)
         / np.sin(a))
    return [da, db, dx, dy]

def get_values(initial_conditions):
    a = solve_ode(ode, initial_conditions, time_values, 0)
    b = solve_ode(ode, initial_conditions, time_values, 1)

    x = L * np.sin(a) * np.cos(b)
    z = L * np.sin(a) * np.sin(b)
    y = - L * np.cos(a)
    y = 43 + abs(minimum(y)) - L * np.cos(a)

    return x, y, z

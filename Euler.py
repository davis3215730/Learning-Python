import numpy as np
import matplotlib.pyplot as plt

# 1st order ODE solver
# Euler's method:
    # dv/dt = F(t,v)
    # v(t0) = v0    *initial conditions*

# FUNCTION PARAMS
tau = 10
Fc = 10
m = 0.5
mu = 2
F = lambda t, v: (-mu*v + Fc*np.exp(-t/tau)) / m
# TEST INPUTS
dt = 0.1
ti = 0
tf = 5
tN = np.arange(ti, tf, dt)
v0 = 1

# Preallocate for speed
vN = np.zeros(len(tN))
vN[0] = v0

for t in range(0, len(tN) - 1):
    # for each value of time get consequent x
    # last x does not need to be evaluated further : len(tN) - 1
    slope = F(tN[t], vN[t])         # diff eqn is equal to slope
    vN[t + 1] = vN[t] + dt*slope    # solve for the consequent x's and store each consequent Nth x

# plot stuff
plt.plot(tN, vN, 'bo--', label='Euler')             # Euler solution
# plt.plot(tN, , 'r', label='Analytical')   # analytical solution
plt.title('Euler Solution for Simple ODE')
plt.xlabel('t')
plt.ylabel('v')
plt.grid()
plt.show()



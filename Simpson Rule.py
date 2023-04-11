import numpy as np
import matplotlib.pyplot as plt


a = 0          # lower bound
b = 1     # upper bound
h = 0.1     # step size
N = (b-a) / h   # number of trapezoids
N = int(N)

# generate variables
x = [i/N for i in range(N+1)]
f = x*np.exp(x)

fk = np.zeros(N-1)     # preallocate
for i in range(N-1):     # middle outputs
    fk[i] = f[i+1]

f0 = f[0]   # first output
fN = f[-1]  # last output

# compute middle section for area
for k in range(len(fk)):
    if (k % 2) == 0:
        # even number but odd element
        fk[k] = 4*fk[k]
    else:
        # odd number but even element
        fk[k] = 2*fk[k]

print(fk)

Area = (h/3) * (f0 + sum(fk) + fN)
print(Area)

plt.plot(x,f,'b')
plt.grid()
plt.show()
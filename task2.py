import numpy as np
from scipy.integrate import quad

def f(x):
    return x**2

a, b = 0, 2

N = 10000
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)

points_under_curve = y_random < f(x_random)
area_mc = (b - a) * f(b) * np.mean(points_under_curve)

area_exact, _ = quad(f, a, b)

print(f'Monte Carlo method: {area_mc}')
print(f'Quad integral (exact value) {area_exact}')
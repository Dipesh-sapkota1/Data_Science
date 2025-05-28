import math

x = 1.2


a = math.sin(x**2) - math.cos(x**3)
b = math.exp(x) / (x**2 + 1)

c = a + b

print(f"Output: {c:.2f}")
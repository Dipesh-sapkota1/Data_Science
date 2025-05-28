import math

x = 2

a = math.log(x**2 + 1) / math.sqrt(1 + (math.sin(x)**2))
b = math.exp(x * math.cos(x))

c = a + b

print(f"Output: {c:.2f}")
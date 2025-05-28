import math

x = 4

a = math.exp(math.sqrt(x))
b = math.log10(x**2 + 10 * x + 25)
c = math.sin(x/2)

d = a + b - c

print(f"Output: {d:.2f}")


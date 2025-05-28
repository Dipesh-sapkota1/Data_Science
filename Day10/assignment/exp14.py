import math

x = 3
y = 4


a = (x + y )**2 / math.log10(x**2 + y**2 + 1)
b = math.sin(x * y)
c = math.cos(x - y)
d = a + b + c

print(f"Output: {d:.2f}")


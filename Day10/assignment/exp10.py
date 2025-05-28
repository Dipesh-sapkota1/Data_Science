import math

x = 2
y = 3

a = math.exp(x + y) + math.cos(x * y)
b = math.sqrt(x**2 + y**2)
c = math.log(x + y + 1)

d = (a / b) + c

print(f"Output: {d:.2f}")
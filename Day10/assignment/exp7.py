import math

x = 5
y = 2


a = (x**3 + y**3) / (x + y)
b = math.log(x * y)
c = math.sqrt(x**2 - y**2)

d = a + b + c

print(f"Output: {d:.2f}")


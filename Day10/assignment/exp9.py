import math

x = 9
y = 7

a = math.log2(x**2 + y**2)
b = math.sqrt(x + y)
c = math.tan((x - y)/2)

d = (a / b) + c

print(f"Output: {d:.2f}")
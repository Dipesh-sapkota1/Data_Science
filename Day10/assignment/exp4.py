import math

x = math.pi / 6

a = math.tan(x)
b = math.sin(x**2) / (1 + math.cos(x**3)) 
c = math.sqrt(x**4 + 16)

d = a + b + c

print(f"Output: {d:.2f}")

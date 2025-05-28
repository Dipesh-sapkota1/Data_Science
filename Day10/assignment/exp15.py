import math

x = 1
y = 2
z = 3

a = math.sqrt(x**2 + y**2  + z**2) / math.tan(x)
b = math.log(x * y + y * z + z * x)
c = a + b 

print(f"Output: {c:.2f}")


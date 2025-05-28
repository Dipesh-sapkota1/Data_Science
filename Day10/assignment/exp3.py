import math

x = 3
y = 4

 
a =  math.sqrt(x**2 + y**2)
b = math.log10(x * y) + math.exp(x + y)
c = a + b  

print(f"Output: {c:.2f}")
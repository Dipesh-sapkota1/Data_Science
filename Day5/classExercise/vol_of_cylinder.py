import math

def vol(r,h):
    return math.pi*r**2*h

radius=int(input('Enter radius: '))
height=int(input('Enter height: '))
print(f'volume is: {vol(radius,height):.2f}')
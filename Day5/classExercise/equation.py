import math

def equ(r,h):
    return math.exp(h) + math.log10(r -1)

radius=int(input('Enter radius: '))
height=int(input('Enter height: '))
print(f'Equation: {equ(radius,height):.2f}')
import math

def vol_hemi(r):
    return 2/3*(math.pi * r**3)
def vol_sphere(r):
    return 4/3*(math.pi * r**3)

radius=float(input("Enter the radius: "))

print(f"volume of sphere is: {vol_sphere(radius):.2f}")
print(f"volume of hemisphere is: {vol_hemi(radius):.2f}")

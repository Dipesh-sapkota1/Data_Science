import math


def vol_cone(r, h):
    heightCone = math.sqrt(h**2 - r**2)
    return (math.pi*r**2*heightCone) / 3


def vol_cy(r, h):
    return math.pi*r**2*h


conehypo = float(input("Enter hypotenous of cone: "))
cylinderHeight = float(input("Enter height of cylinder: "))
radius = float(input("Enter radius of solid figure: "))

combined_vol = vol_cone(radius, conehypo) + vol_cy(radius, cylinderHeight)
print(f"Volume of combiled solid: {combined_vol:.2f}")

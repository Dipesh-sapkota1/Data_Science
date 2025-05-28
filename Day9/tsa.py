import math

def cal(part):
    radius = float(input("Enter radius: "))
    height = float(input("Enter height: "))
    pi = math.pi

    match part:
        case 'volume':
            volume = lambda radius, height: pi * radius**2 * height + (2/3) * pi * radius**3
            return round(volume(radius,height),2)
        case 'area':
             area = lambda radius, height: 3 * pi * radius**2 + 2 * pi *radius *(radius + height)
             return round(area(radius,height),2)
        case _:
            return 'INVALID'



print(f"the TSA of combined solid is {cal('area')},cm² and volume {cal('volume')},cm3")



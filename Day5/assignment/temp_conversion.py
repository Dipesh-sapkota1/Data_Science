opt = int(input("1. Celcius to fahernheit\n2. Fahernheit to celcius\n: "))


def to_fahrenheit(c):
    return (9/5 * c) + 32


def to_celcius(f):
    return (f - 32) * 5/9



if (opt == 1):
    celcius = float(input("Enter celcius: "))
    print(f"F = {to_fahrenheit(celcius):.2f}°F")
elif(opt == 2):
    fahrenheit = float(input("Enter fahrenheit: "))
    print(f"C = {to_celcius(fahrenheit):.2f}°C")








 
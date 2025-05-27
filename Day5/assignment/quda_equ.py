import math

# Input values
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("No real roots")
else:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)

    print(f"The roots are: {root1} and {root2}")

    # Optional: Verify the roots
    def eval_eq(x):
        return a * x**2 + b * x + c

    print(f"Verification: f({root1}) = {eval_eq(root1)}")
    print(f"Verification: f({root2}) = {eval_eq(root2)}")

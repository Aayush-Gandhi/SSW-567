from math import isclose, isfinite

def classify_triangle(a, b, c):
    
    # Validate numeric, positive, finite inputs
    for x in (a, b, c):
        if not isinstance(x, (int, float)) or not isfinite(x) or x <= 0:
            return "Not a triangle"

    # Sort so c is the largest; helps the right-triangle check
    a, b, c = sorted(map(float, (a, b, c)))
    eps = 1e-9

    # Triangle inequality (strict)
    if a + b <= c + eps:
        return "Not a triangle"

    # Equilateral check
    if isclose(a, b, abs_tol=eps) and isclose(b, c, abs_tol=eps):
        return "Equilateral"

    # Right-triangle check
    if isclose(a*a + b*b, c*c, rel_tol=1e-9, abs_tol=1e-9):
        return "Right"

    # Isosceles (with tolerance)
    if (isclose(a, b, abs_tol=eps) or
        isclose(b, c, abs_tol=eps) or
        isclose(a, c, abs_tol=eps)):
        return "Isosceles"

    return "Scalene"


if __name__ == "__main__":
    try:
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        c = float(input("Enter side c: "))
        print(f"Triangle type: {classify_triangle(a, b, c)}")
    except ValueError:
        print("Not a triangle")

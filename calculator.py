import math

def show_menu():
    print("\nWelcome to Math Formula Calculator!")
    print("1. Area of Circle")
    print("2. Perimeter of Rectangle")
    print("3. Solve Quadratic Equation")
    print("4. Simple Interest")
    print("5. Area of Triangle")
    print("6. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-6" \
    "): ")

    if choice == '1':
        r = float(input("Enter radius: "))
        area = math.pi * r * r
        print("Area of Circle =", area)

    elif choice == '2':
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        perimeter = 2 * (l + w)
        print("Perimeter of Rectangle =", perimeter)

    elif choice == '3':
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        d = (b ** 2) - (4 * a * c)
        if d < 0:
            print("No Real Roots")
        else:
            root1 = (-b + math.sqrt(d)) / (2 * a)
            root2 = (-b - math.sqrt(d)) / (2 * a)
            print("Roots are:", root1, "and", root2)

    elif choice == '4':
        P = float(input("Enter Principal: "))
        R = float(input("Enter Rate: "))
        T = float(input("Enter Time: "))
        SI = (P * R * T) / 100
        print("Simple Interest =", SI)

    elif choice == '5':
        base =  float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print("Area of Triangle =", area)

    elif choice == '6':
        print("Thanks for using!")
        break

    else:
        print("Invalid choice. Try again.")
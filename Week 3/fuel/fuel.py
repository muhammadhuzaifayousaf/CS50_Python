while True:
    fuel = input("Fraction: ")

    try:
        a, b = fuel.split('/')
        x = int(a)
        y = int(b)
        f = x / y
        if f <= 1:
            break

    except (ValueError, ZeroDivisionError):
        pass

percent = round(f*100)
if percent <= 1:
    print("E")
elif percent >= 99:
    print("F")
else:
    print(f"{percent}%")

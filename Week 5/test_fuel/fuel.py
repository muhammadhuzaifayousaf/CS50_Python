def main():
    while True:
        fuel = input("Fraction: ")

        try:
            percent = convert(fuel)
            break
        except (ValueError, ZeroDivisionError):
            pass

    print(gauge(percent))


def convert(fraction):
    try:
        a, b = fraction.split('/')
        x = int(a)
        y = int(b)

        if y == 0:
            raise ZeroDivisionError("Division by zero")
        if x > y:
            raise ValueError("Invalid fraction")

        f = x / y
        return round(f * 100)
    except ValueError:
        raise ValueError("Invalid fraction")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()

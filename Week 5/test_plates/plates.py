def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[:2].isalpha():
        return False

    if not s.isalnum():
        return False

    num_started = False

    for i, char in enumerate(s):
        if char.isdigit():
            if not num_started:
                num_started = True
                if char == '0':
                    return False
        elif num_started:
            return False

    return True


if __name__ == "__main__":
    main()

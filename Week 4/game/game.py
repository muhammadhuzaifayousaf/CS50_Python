import random


def main():
    level = get_int("Level: ")
    range = random.randint(1, level)

    while True:
        guess = get_int("Guess: ")
        if guess < range:
            print("Too small!")
        elif guess > range:
            print("Too large!")
        else:
            print("Just right!")
            break


def get_int(number):
    while True:
        try:
            num = int(input(number))
            if num > 0:
                return num

        except ValueError:
            pass

        print("Please enter a positive integer.")


if __name__ == "__main__":
    main()

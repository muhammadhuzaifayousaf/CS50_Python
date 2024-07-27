def main():
    s = input("camelCase: ")
    convert = snake_case(s)
    print('')


def snake_case(s):
    print("snake_case: ")
    for character in s:
        if character.isupper():
            print('_' + character.lower(), end="")
        else:
            print(character, end="")


main()

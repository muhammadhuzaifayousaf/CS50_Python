def main():
    str = input("")
    convert(str)


def convert(str):
    print(str.replace(":)", "🙂").replace(":(", "🙁"))


main()

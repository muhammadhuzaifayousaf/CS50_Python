def main():
    time = input("What time is it? ")
    meal = convert(time)
    if 7.0 <= meal <= 8.0:
        print("breakfast time")
    elif 12.0 <= meal <= 13.0:
        print("lunch time")
    elif 18.0 <= meal <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hrs = int(hours)
    mins = int(minutes)
    total = hrs + mins / 60
    return total

if __name__ == "__main__":
    main()

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


while True:
    date = input("Date: ").strip()

    try:
        month, day, year = date.split('/')
        month = int(month)
        day = int(day)
        year = int(year)
        if 1 <= month <= 12 and 1 <= day <= 31:
            break
    except (ValueError, IndexError):
        try:
            month_old, day_old, year = date.split(' ')
            if day_old.endswith(","):
                day = day_old[:-1]
                if day.isdigit() and year.isdigit():
                    day = int(day)
                    year = int(year)
                    if 1 <= day <= 31:
                        for i, month_name in enumerate(months):
                            if month_old == month_name:
                                month = i + 1
                                break
                        else:
                            continue
                        if 1 <= month <= 12:
                            break
        except (ValueError, IndexError):
            pass

print(f"{year}-{month:02}-{day:02}")

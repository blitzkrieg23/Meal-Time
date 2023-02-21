def convert(time_str):
    hours, minutes = map(int, time_str.split(":"))

    if "p.m." in time_str and hours != 12:
        hours += 12
    elif "a.m." in time_str and hours == 12:
        hours = 0


    return hours + minutes / 60

def meal(time):
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def main():
    time_str = input("Enter time: ")
    time = convert(time_str)
    meal(time)

if __name__ == "__main__":
    main()
time=input("what time is it? ").split(":")
def main():
    Total=convert(time)
    if 7<=Total<=8:
        print("Breakfast time")
    elif 12<=Total<=13:
        print("Lunch time")
    elif 18<=Total<=19:
        print("Dinner time")

def convert(Time):
    Time=int(time[1])/60
    Total=int(time[0])+Time
    return Total

if __name__ == "__main__":
    main()

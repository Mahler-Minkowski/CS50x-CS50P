import re
months={"January":"01",
    "February":"02",
    "March":"03",
    "April":"04",
    "May":"05",
    "June":"06",
    "July":"07",
    "August":"08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12"
}
#MM/DD/YYYY 1630-09-09
#MM D, YYYY
while True:
    date=input("type in dates")
    try:
        if len(date.split("/")) == 3:
            date=date.split("/")
            if (1<=int(date)[0]<=12 and 1<=int(date[1])<=30):
                if int(date[0])<10:
                    if int(date[1])<10:
                        print(date[2]+"-0"+date[0]+"-0"+date[1])
                    else:
                        print(date[2]+"-0"+date[0]+"-"+date[1])
                else:
                    if int(date[1])<10:
                        print(date[2]+"-"+date[0]+"-0"+date[1])
                    else:
                        print(date[2]+"-"+date[0]+"-"+date[1])
        elif len(re.split(r'[, ]',date))==3:
            date=re.split(r'[, ]',date)
            if date[0] in months:
                if 1<=int(date[1])<=9:
                    print(date[2]+"-"+months[date[0]]+"-0"+date[1])
                elif 10<=int(date[1])<=30:
                    print(date[2]+"-"+months[date[0]]+"-"date[1])
    except ValueError:
        pass

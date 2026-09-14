import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time=r'(?:1[0-1]|[0-9]):?(?:[0-5][0-9])? [AP]M'
    if match:=re.search(rf'({time}) to ({time})',s):
        match_1=str(numcvt(cmple(match.group(1))))
        match_2=str(numcvt(cmple(match.group(2))))
        return f'{match_1.zfill(5).strip()} to {match_2.zfill(5).strip()}'
    else:
        raise ValueError

def cmple(s):
    if not ':' in s:
        return (s+':00').replace(' ','')
    else:
        return s

def numcvt(s):
    if "AM" in s:
        return s.replace('AM','')
    elif 'PM' in s:
        hour=re.search(r'(1[0-1]|[0-9])(:[0-5][0-9])?',s)
        hour_1=int(hour.group(1))+12
        return f"{hour_1}{hour.group(2)}"



if __name__ == "__main__":
    main()

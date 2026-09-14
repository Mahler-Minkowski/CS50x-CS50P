import datetime as dt
from num2words import num2words
date_present=dt.date.today()
try:
    date_birth=dt.date.fromisoformat(input('Date of birth: '))

    sbtr=round(int((date_present - date_birth).total_seconds())/60)
except ValueError:
    print('Invalid date')
else:
    print(f'{num2words(sbtr)} minutes')

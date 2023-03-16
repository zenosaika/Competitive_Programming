# https://www.borntodev.com/devlab/task/891

import datetime

days = ['Monday', 'Tuesday', 'Thursday', 'Wednesday', 'Friday', 'Saturday', 'Sunday']
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']

year = int(input())
print(f'year: {year}')

for i, month in enumerate(months, 1):
  for j in range(1, 7):
    day = days[datetime.datetime(year, i, j).weekday()]
    if day == 'Monday' or day == 'Tuesday':
      print(f'{month}: {day} {j}')
      break
      
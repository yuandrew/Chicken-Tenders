"""
    Author: Andrew Yuan
    Date: Jan 30, 2019
    Purpose: To eat more chicken tenders
"""
from urllib.request import urlopen
from datetime import datetime


bursley = 'https://dining.umich.edu/menus-locations/dining-halls/bursley/'
mojo = 'https://dining.umich.edu/menus-locations/dining-halls/mosher-jordan/'
nq = 'https://dining.umich.edu/menus-locations/dining-halls/north-quad/'
sq = 'https://dining.umich.edu/menus-locations/dining-halls/south-quad/'
letterMonth = [
    '',
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

def search(dining_url, hall, day, month, year, num):
    dining_url += '?menuDate={}-{}-{}'.format(year, month, day)
    page = urlopen(dining_url).read().decode('utf-8')
    # if "Chicken Tenders" in soup:
    if "Chicken Tenders" in page:
        print("Chicken Tenders found at {} on {} {}.".format(hall, letterMonth[num], day))


day = datetime.now().day - 2
month = datetime.now().month
year = datetime.now().year

"""
dining_url = 'https://dining.umich.edu/menus-locations/dining-halls/mosher-jordan/?menuDate=2019-01-29'
page = urlopen(dining_url).read().decode('utf-8')
print('Chicken Tenders' in page)
"""

for i in range(30):
    if day > 31:
        month += 1
        day = 1
    if day < 10:
        strDay = '0' + str(day)
    else:
        strDay = str(day)
    if month < 10:
        strMonth = '0' + str(month)
    else:
        strMonth = str(month)

    # print("{} {}, {}".format(letterMonth[month], day, year))

    search(bursley, "Bursley", strDay, strMonth, str(year), month)
    search(mojo, "Mojo", strDay, strMonth, str(year), month)
    search(nq, "North Quad", strDay, strMonth, str(year), month)
    search(sq, "South Quad", strDay, strMonth, str(year), month)
    day += 1

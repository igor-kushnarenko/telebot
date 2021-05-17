from ics import Calendar, Event
import requests

# url = 'https://calendar.google.com/calendar/ical/jo7qlqrl35rr92s1409ke83c9k%40group.calendar.google.com/public/basic.ics'
# cal = Calendar(requests.get(url).text)
#
# with open('my.ics', 'w') as my_file:
#     my_file.writelines(cal)


with open('calendar.txt', 'r', encoding='utf-8') as f:
    cal = f.readlines()

result = []

for x in cal:
    if 'DTSTART' in x:
        result.append(x)



print(sorted(result))
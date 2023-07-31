import time
from datetime import datetime
print(datetime.now())

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

hour = int(time.strftime('%H'))
print(hour)

seconds = int(time.strftime('%S'))
print(seconds)

minute = int(time.strftime('%M'))
print(minute)

if hour >= 5 and hour < 12:
    print("Good Morning!")
elif hour >= 12 and hour < 18:
    print("Good Afternoon!")
else:
    print("Good Evening!")

# Q: Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you:

import time     # A time module         # https://docs.python.org/3/library/time.html#time.strftime

timestamp = time.strftime("%H:%M:%S")       # format for time 
print(timestamp)

hour = int(time.strftime("%H"))
print(hour)
minute = int(time.strftime("%M"))
print(minute)
sec = int(time.strftime("%S"))
print(sec)


if(hour > 5 and hour <=12):
    if(minute < 30):
        print('Good morning')
elif(hour >12 and hour <= 17):
    if(minute == 0 and minute > 30):
        print('Good afternoon')
elif(hour > 17 and hour <= 24):
    if(minute >10):
        print('Good Night')
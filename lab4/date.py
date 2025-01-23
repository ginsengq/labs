#ex1
import datetime

x = datetime.datetime.now()
y = x - datetime.timedelta(days = 5)
print(y.strftime("%x"))


#ex2
import datetime

x = datetime.datetime.now()
yesterday = x - datetime.timedelta(days = 1)
today = x
tomorrow = x + datetime.timedelta(days = 1)
print(yesterday.strftime("%x"))
print(today.strftime("%x"))
print(tomorrow.strftime("%x"))


#ex3
import datetime

x = datetime.datetime.now()
y = x.replace(microsecond = 0)
print(y)


#ex4
import datetime

def d(date1, date2):
    delta = date2 - date1
    return delta.total_seconds()

x = input()
y = input()
date_format = "%y-%m-%d %H:%M:%S"

date1 = datetime.datetime.strptime(x, date_format)
date2 = datetime.datetime.strptime(y, date_format)

diff = int(d(date1, date2))
if diff < 0:
    diff = -diff
print("Two date difference in seconds: ", diff)



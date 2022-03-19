import random
import datetime

strdate1=input("enter a date (YYYY-MM-DD)")
strdate2=input("enter a date (YYYY-MM-DD)")

date1=datetime.datetime.strptime(strdate1, '%Y-%m-%d')
date2=datetime.datetime.strptime(strdate2, '%Y-%m-%d')

epoch1=date1.timestamp()
epoch2=date2.timestamp()

rand_epoch=random.randint(epoch1,epoch2)

new_date = datetime.datetime.fromtimestamp(rand_epoch)
week_day= new_date.weekday()

print(new_date.strftime('%Y-%m-%d'))
if week_day==2:
    print("I have no vinaigrette!")

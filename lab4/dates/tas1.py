import datetime

date_now = datetime.datetime.now()
new_date = date_now - datetime.timedelta(days=5)

print(new_date)

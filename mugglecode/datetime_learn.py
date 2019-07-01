from datetime import datetime
from datetime import timedelta


date_now = datetime.today()
print(date_now)
date_week_ago = date_now - timedelta(days=7)
print(date_week_ago)

d = "2017-06-25T19:36:36Z"

if str(date_now) > d and str(date_week_ago) > d:
    print('done')
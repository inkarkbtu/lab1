from datetime import datetime
c = datetime.now()
x = datetime(c.year, c.month, c.day-5)
print((c-x).total_seconds())
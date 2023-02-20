from datetime import datetime, timedelta
today = datetime.now()
# print(today.strftime("%f"))
print(today.replace(microsecond=0))
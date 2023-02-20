from datetime import datetime, timedelta

today = datetime.now()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)

print("Yesterday:", yesterday.strftime("%b %d"))
print("Today:", today.strftime("%b %d"))
print("Tomorrow:", tomorrow.strftime("%b %d"))
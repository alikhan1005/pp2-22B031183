from datetime import datetime, timedelta

data = datetime.now()
five_ago = data - timedelta(days=5)

print("five days ago was:" , five_ago)


from datetime import datetime

now = datetime.now()
print(now)

f = now.strftime("%Y-%m-%d %H:%M:%S")
print(f)
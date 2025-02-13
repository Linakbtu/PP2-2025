from datetime import datetime, timedelta

today = datetime.today()
five_days_ago = today - timedelta(days=5)

print("Date 5 days ago:", five_days_ago.date())

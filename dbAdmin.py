import requests
from datetime import datetime, timedelta
from cs50 import SQL
db = SQL('sqlite:///clinic.db')
print(datetime.now().strftime('%Y-%m-%d'))
date = db.execute('SELECT * FROM appointments WHERE id = ?', 1)[0]['booked_date']
date = datetime.strptime(date, '%Y-%m-%d')
print(date.strftime('%Y'))
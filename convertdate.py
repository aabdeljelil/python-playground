# by Anissa and Pratyusha 
from datetime import datetime
# set a variable birthday = "1-May-12"
birthday = "1-May-12"

#Parse the date using datetime.datetime.strptime

#raw_date = "2012-05-01"
date_format = "%d-%B-%y"

parsed_date = datetime.strptime(birthday, date_format)
date_str = parsed_date.strftime("%-m/%-d/%Y") # 5/1/2012
print(date_str)


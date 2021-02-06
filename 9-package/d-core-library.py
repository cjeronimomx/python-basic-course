# Firts import type
import os
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
log = logging.getLogger("core-library")
log.info("Executing ls -ltr")

os.system("ls -ltr")




# Second import option
from collections import deque

queue = deque([1, 2, 3, 4])
print(queue)


# Third import example
from math import ceil as round_ceil
from math import floor as round_floor
# from math import ceil as round_ceil, floor as round_floor

print(round_ceil(2.3))
print(round_floor(2.9))



# List libraries/package/modules core
"""
> python
>>> help()
help> modules
"""




# Other core libraries
from collections import Counter
sentence = "How many times does each word show up in this text"
counter = Counter(sentence.split())
print(counter)
print(counter.most_common())


import datetime
course_time = datetime.time(hour=16, minute=0, second=1, microsecond=2)
print(course_time)
print(course_time.hour)
print(course_time.minute)

course_date = datetime.date(year=2021, month=2, day=2)
print(course_date)
print(course_date.year)
print(course_date.month)

my_date = datetime.datetime(2021, 2, 3, 18, 0, 0)
print(my_date)
print(my_date.strftime("%H:%M:%S"))
print(my_date.strftime("%d-%m-%Y")) # y or Y

now = datetime.datetime.now()
print(now)
print(now.time())
print(now.date())
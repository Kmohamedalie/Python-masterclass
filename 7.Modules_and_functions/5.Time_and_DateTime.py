# *********************************************************************
#                    Time and DateTime                                #
# *********************************************************************

# working with time module
import time

"""
# UTC time
print(time.gmtime(0))
# local time
print(time.localtime())
# in numeric
print(time.time())

print()
print("*" * 40)

time_here = time.localtime()
print(time_here)
print("Year: ", time_here[0], time_here.tm_year)
print("Month: ", time_here[1], time_here.tm_mon)
print("Day: ", time_here[2], time_here.tm_mday)
"""

from time import perf_counter as my_timer # time, monotonic
import random

input("Press enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input('Press enter to stop')

end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds".format(end_time - start_time))

print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))

print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("\tDaylight Saving Time is in effect for this location")
    print("\tThe DST timezone is " + time.tzname[1])

print("local time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("UTC time is   " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))

# It is divisible by 4
#
# Except years divisible by 100 → these are not leap years
#
# Unless the year is also divisible by 400 → then it's a leap year again
from ctypes.wintypes import LARGE_INTEGER

year = int(input("Enter a year: \n"))
if (year%4 == 0 and year%100 != 0) or (year%400==0):
    print("Its a leap year")
else:
    print("its not a leap year")
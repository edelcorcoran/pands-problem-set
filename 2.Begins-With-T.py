#Edel Corcoran 
#Is today a day that begins with the letter T?
#Adapted from Tuesday.py 

import datetime

if datetime.datetime.today().weekday() == 1 or 3:
    print("Yes! Today is a day that starts with the letter T")
else:
    print("No! Today is not a day that starts with the letter T")

    
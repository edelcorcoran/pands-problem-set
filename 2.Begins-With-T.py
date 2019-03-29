#Edel Corcoran Begins With T program

#Program will determine whether today a day that begins with the letter T?
#References: Adapted from Tuesday.py 


#Program imports the current weekday and determines answer "Yes!..." or "No!...."
import datetime as dt
    
if dt.datetime.today().weekday() == 1 or 3:
    print("No! Today is not a day that starts with the letter T")
else:
    print("Yes! Today is a day that starts with the letter T")



    
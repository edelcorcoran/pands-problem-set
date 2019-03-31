

# Edel Corcoran Solution 7
#Program calculates an approximate square root of a positive float number selected by user.
#References/Adapted from: https://www.programiz.com/python-programming/examples/square-root 

#Import math function
import math

# User requested to input an number. 
n = float(input("Input a Positive Number: "))
#Code ensure n must be greater than zero by printing message and exiting program
if n <= 0:
    print("Unfortunately this is not a positive number.")  #Notifies User if they input a negative number    
    quit()      #Exits the program
 
while n > 0:
    n = float(n)        #code ensure n is positive float

    number_sqrt = n ** 0.5   

    print("The Square Root of Floating point number %0.1f is approx %0.1f" %(n, number_sqrt)) #Code gives square root to 1 decimal place

    break       #stop repeated printing
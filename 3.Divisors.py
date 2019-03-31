#Edel Corcoran Solution 2 from Problem Sheet 
#Programming & Scripting H.Dip Data Analytics

# References: Code examples in lecture videos on Statements and Controlled Loops 
# Adapted from https://www.sanfoundry.com/python-program-print-numbers-range-divisible-given-number/ 31/3/19

#Range at start works
# Working but not printing number!!


#Provide the range to be searhed ie.from 1000 (lower) to 10000 (upper)
lower = 1000
upper = 10000

#Provide the divisors 6 and 12 
a=6
b=12

for i in range(lower,upper+1):
    if(i%a ==0) and (i%b ==0):
        print(i)
        
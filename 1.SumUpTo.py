#Edel Corcoran Solution 1: Python Sum Up To Program 

#Program will give the sum of all numbers between 1 and a positive integer provided by user

#References/adapted from:https://www.w3resource.com/python-exercises/python-basic-exercise-58.php

# User inputs any positive integer
n = int(input("Enter a positive integer: "))
for i in range(1,n):        #range is between 1 and number input by user
    sum_num = sum(range(1,n))       #sum function to sum numbers in range
print(sum_num)                  #print answer






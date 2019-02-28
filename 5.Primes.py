#Edel Corcoran 

#Adapted from (https://stackoverflow.com/questions/18833759/python-prime-number-checker)

#Not Working Correct Yet!

a=2
num=int(input("Please enter an integer: "))

while num>a:
    if num%a==0 & a!=num:
        print('Is not Prime Number')
        break
    else:
        print('Is a Prime Number')
        a=(num)+1



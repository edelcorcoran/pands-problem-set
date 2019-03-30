#Edel Corcoran Solution 4 Collatz.py

# User inputs a number into the program, if it's even then the number is divided by 2, if the number is odd then it's multiplied by 3 and 1 is added. this continues until the program reached 1.
# References/Adapted from: https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff, https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff

def collatz(number):
    while number != 1:
        if (number % 2 == 0):       #When it's an even number divide by 2
            number = number // 2 
        else:                 
            number = number * 3 + 1     #When it's an odd number multipy by 3 and add 1
        print (number)
        return (number)

try:
    n = int(input('Enter a positive integer: '))        #User asked to input number
    while (n != 1):     # Loops until n = 1
        n = collatz(int(n))
except ValueError:
    print('Enter a valid integer')      #Error message if invalid integer is entered

#Edel Corcoran Solution 4 Collatz.py

# User inputs a number into the program, if it's even then the number is divided by 2, if the number is odd then it's multiplied by 3 and 1 is added. this continues until the program reached 1.
# References/Adapted from: https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff

#User inputs a number
def collatz(number):
    if (number % 2 == 0): 
        number = number // 2 
    else:                 
        number = number * 3 + 1
    print (number)
    return (number)

n = int(input('Enter a positive integer: '))
while (n != 1):
    n = collatz(n)
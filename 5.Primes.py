#Edel Corcoran 

#Adapted from (https://stackoverflow.com/questions/18833759/python-prime-number-checker), https://www.javatpoint.com/python-check-prime-number



a=2
num=int(input("Please enter a positive integer: "))     #User requestef to input a positive integer

def prime(num):         #define function to evaluate if users number is prime or not
    while num == a:
        print('2 Is the only even Prime Number')
        break           #stop result being repeatedly printed
    while num>a:
        for i in range(2,num):      #for any number great than 2
            if (num % i) ==0:
                print(num,'Is not a Prime Number')
                break       #stop result being repeatedly printed
        else:
            print(num,'Is a Prime Number')
            break       #stop result being repeatedly printed
        
prime(num)
 

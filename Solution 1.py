#Solution to Problem 1
#Edel Corcoran 
#Calculate the sum of all numbers between 1 and n (a positive integer).

n = int(input("Enter a positive integer: "))
for i in range(1,n):
    sum_num = sum(range(1,n))
print(sum_num)
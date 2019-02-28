#Edel Corcoran Solution 2 from Problem Sheet 
#Programming & Scripting H.Dip Data Analytics

# Adapted from Code examples in lecture videos on Statements and Controlled Loops

#Range at start works
# Working but not printing number!!

for n in range(1000, 10000):
    if n%6 == 0:
        print("n, is divisible by 6 but not 12")
    elif n%12 == 0:
        print()
    else:
        print()
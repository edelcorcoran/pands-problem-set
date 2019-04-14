# Approximate a Square Root Using Newton's Method

#The number to calculate the square root of.
rootof = 64    
#A initial estimate for the square root
estimate = 6   


 #input the acceptable range. Keep going until the estimate squared is within 0.1 of rootof.
 #Absolute value turns negative numbers to their positive version and leaves positives numbers unchanged.
while abs((estimate*estimate) - rootof) > 0.1:      
    #This is Newton's Methodto improve our estimate.
    estimate -= ((estimate * estimate) - rootof)/(2 * estimate)     

print(f"The square root of {rootof} is approx. {estimate}.")        #Print estimated approx sq root
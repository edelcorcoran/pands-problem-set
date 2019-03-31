# Edel Corcoran Solution 6 SecondString.py

# Program takes a user input string and outputs very second work

# References/Adapted from: https://stackoverflow.com/questions/47085552/replace-every-second-word-with-the-word-hello-using-a-function

string = input("Create your own sentence")      # instruct user to input a sentence of their choosing

# format to skip every second word in the user's sentence
#Use the split method to create a list. Then loop over the list with using enumerate which creates a counter.

skip = " ".join(["{} ".format(word)         
        for idx, word in enumerate(string.split())  
        if idx % 2 == 0])
# prints every second word in users sentence
print(skip)
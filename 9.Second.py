
#Edel Corcoran Solution 9

# Write a program that write in a text file and outputs every second line. 

#Reference for txt: http://www.online-literature.com/melville/mobydick/2/
#Adapted from: https://stackoverflow.com/questions/30551945/how-do-i-get-python-to-read-only-every-other-line-from-a-file-that-contains-a-po
#Other references: https://www.youtube.com/watch?v=0EgSo7hsRWM viewed 31/3/19, https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python

import sys

with open('9.MobyDick.txt','r') as inputfile:       #inputfile   .... identifies the text file '9.Moby..' which located in the same folder as the script and opens it 'r' in read mode
    count = 0                           #start from first line
    for line in inputfile:
        count+=1
        if count % 2 == 0: #print even lines....divisible by 2 with remainder zero
            print(line)

inputfile.close()       #close program when finished



# Ref: https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
# readline()     ... to read a file line by line – as opposed to pulling the content of the entire file at once
# file = open(“9.MobyDick.txt”, “r”)  .....  to print file.readline(x) .....will print the xth line in the file
# file.read()    .... to extract a string that contains all characters in the file
# {,}    ....EOL end of line



# Ref: https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
# readline()     ... to read a file line by line – as opposed to pulling the content of the entire file at once
# file = open(“9.MobyDick.txt”, “r”)  .....  to print file.readline(x) .....will print the xth line in the file
# file.read()    .... to extract a string that contains all characters in the file


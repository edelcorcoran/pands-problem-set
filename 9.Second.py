
#Edel Corcoran Solution 9

# Write a program that write in a text file and outputs every second line. 

#Reference for txt: http://www.online-literature.com/melville/mobydick/2/
#Adapted from: https://www.youtube.com/watch?v=0EgSo7hsRWM viewed 31/3/19

file = open('9.MobyDick.txt','r')       #identifies the text file '9.Moby..' which located in the same folder as the script and opens it 'r' in read mode
f=file.readlines()      #to enable us to read the contents of the file

new_list =[]            #this code is for extracting all words from a text file....not a sentence...need to alter
for line in f:
    if line [-1] == '\n':           #python prints \n after each word. This code removes the \n
        new_list.append(line[:-1])      #'new_list.append.(line.strip())' is a shorter version
    else:
        new_list.append(line)
print(new_list)
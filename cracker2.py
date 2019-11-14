# Find and open the password file and dictionary file
#  <your code goes here>

# Identify users whose password appears in the dictionary file
# <your code goes here>

# Print the list
import hash 
import sys
lines = open('potter_hashed.txt').read().splitlines()
word_lines = open('words.txt').read().splitlines()

usernames=[]
passwords=[]
words=[]

for line in lines:
    split_lines = line.split(':')
    usernames.append(split_lines[0])
    passwords.append(split_lines[1])

for word_line in word_lines:
    hashed_word = hash.hash(word_line)
    if hashed_word in passwords:
        pw_index = passwords.index(hashed_word)
        
        print(usernames[pw_index]  + ':' + word_line)
    
    


   

#for user in usernames:
#    hashed_user = hash.hash(user)
#    if hashed_user in passwords:
#        print(user)
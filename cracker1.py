# Find and open the password file and dictionary file
#  <your code goes here>
import hash 
import sys
lines = open('potter_hashed.txt').read().splitlines()
usernames=[]
passwords=[]

for line in lines:
    split_lines = line.split(':')
    usernames.append(split_lines[0])
    passwords.append(split_lines[1])


#print(usernames)
#print(passwords)

for user in usernames:
    hashed_user = hash.hash(user)
    if hashed_user in passwords:
        print(user)

# Identify users whose password is in the dictionary
# <your code goes here>

# Print the list
#print('hermione')

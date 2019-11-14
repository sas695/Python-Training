import hash 
import sys
lines = open('potter_hashed.txt').read().splitlines()
usernames=[]
passwords=[]

for line in lines:
    split_lines = line.split(':')
    usernames.append(split_lines[0])
    passwords.append(split_lines[1])
    #print(split_lines)
    #print(usernames,passwords)

tries = 0
while tries < 5:
    tries = tries + 1
    username = input('Username: ')
    password = input('Password: ')
    hash_pw = hash.hash(password)
    
    if username in usernames:
            #print(username)
            index = usernames.index(username)
            #print(hash_pw)
            #print(passwords[index])
            if hash_pw == passwords[index]:
                print('Password correct. Welcome!')
                exit()
            else:
                print('Incorrect username/password, try again: ') 
    else:
        if tries < 5:
            print('Incorrect username/password, try again: ')
        else:
            print('Incorrect username/password.')
print('Too many failed login attempts. Sorry.')

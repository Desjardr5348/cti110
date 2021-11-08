word = input()
password = ''
for x in word:
    if(x=='i'):
        password +="1"
    elif(x=='a'):
        password+= "@"
    elif(x=='m'):
        password+="M"
    elif(x=="B"):
        password+="8"
    elif(x=="s"):
        password+="$"
    else:
        password+=x
password+="!"
print(password)
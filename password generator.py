import random 
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols= "{}+?@$!#^&*()"
all=lower+upper+numbers+symbols
length=9
for i in range(5):
    password="".join(random.sample(all,length))
    print(password)
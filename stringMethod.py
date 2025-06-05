import string
string='helloworld'
print(string.capitalize())
print(string.upper())
print(string.lower())
print(string.replace('w','W'))



str1= string[:4]
str2= string[6:]
print(str1)
print(str2)
print(str1+'W'+str2)


#-----------------------------------------------

string1= 'ola ola ola'
print(string1.count('ola'))

'''OR'''

string2= 'ola ola ola'
count=0
for i in range(len(string2)):
    if string2[i:i+3]=='ola':
        count+=1
print(count)        

#----------------------------------------------------

string3='welcome python'
print(string3.index('o'))

#strip-l strip-r strip

string4= ' hello how are you '
print(string4.strip())
print(string4.lstrip())
print(string4.rstrip())

#------------------------------------------------------

#Startswith-endswith

str1='what are you doing now'

print(str1.startswith('wha'))

print(str1.startswith(str1))  #interviws Q

#------------------------------------------------------

string1="abc"
print(string1.isalnum())


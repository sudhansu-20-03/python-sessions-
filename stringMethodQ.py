#wap to extract.
str1='python.anacond@narasit.com'
str2='sudhansu.datascience@google.com'

#Extract first name: sudhansu
#Extract corce: datascinece
#Extract compny:googol

str1='sudhansu.datascience@google.com'
print("first name:",str1[:str1.find('.')])
print("corce name:",str1[str1.find('.')+1: str1.find('@')])
print("compny name:", str1[str1.find('@')+1: str1.find('.',str1.find('.')+1)])


'''st name: sudhansu
corce name: datascience
compny name: google'''



#wap to extract.
str1='4.5657'

print("1st number:",str1[:str1.find('.')])
print("after . number:",str1[str1.find('.')+1:])

'''1st number: 4
after . number: 5657'''
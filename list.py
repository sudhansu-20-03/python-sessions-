list1=[1,2,4,'a','b']
print(list1)

list2=[1,1.2,'apple',True]
print(list2)

list3=[100,100, 100]
print(list3)

list4=[[1,2,3,4]]
print(list4)

#------------------------------------------------------

'''type'''
print(type(list1))

'''max'''
list1=[1,2,3,4]
list2=['a','b','c','d']
#list3=[1,2,3,'a','b','c']
print(max(list1))
print(max(list2))
print(max(list3))

#--------------------------------------------------------
'''length of string'''

list1=[1,2,3,3,4,5]
print(len(list1))

#--------------------------------------------------------
'''in'''

list1=[1,2,3,4,5]

print(1 in list1)
print(2 in list1)
print(3 in list1)
print(4 in list1)
print(5 in list1)
print(6 in list1)

#for genirliz (i in list1)

for i in list1:
    print(i)

#-----------------------------------------------------------

#list1*3= list1 +list1+list1

#-----------------------------------------------------------

'''index'''
#python index starting '0'

list1=[1,2,4,'a','b']
print(list1[0],list1[1],list1[2],list1[3],list1[4])

for i in range(len(list1)):
    print(i,list1[i])

#------------------------------------------------------------
#wap find the element which are having len<3
#list=['apple','ball', 'cat','dog','eye']
#step1-irerate the list using for loop
#step2-apply the if condition len(<element>)<3
#step3-print(element)

list1=['apple','ball', 'cat','dog','eye']
for i in range(len(list1)):
    if len(list1[i])>3:
        print(list1[i])

list2=[[[[[['guddu']]]]]]
list2[0][0][0][0][0][0]

#------------------------------------------------------------
#let given list is [1,2,3,4,5].
#print squara of the list.

list1=[1,2,3,4,5]
for i in list1:
    print(i*i) 

#------------------------------------------------------------
#list1=['hyd','benguluru','delhi']
#output=['Hyd','Benguluru','Delhi']

list1=['hyd','benguluru','delhi']
for i in list1:
    print(i.capitalize())


#list1=['h#d','beng#luru','delhi']
#output=['h#d','beng#Luru']

list1=['h#d','beng#luru','delhi']
for i in list1:
    if '#' in i:
        print(i.replace('l','L'))

#---------------------------------------------------------------
'''List Comprehenshion'''#write the on single line
#[<output> <forloop>] 
#ex-
'''list1=[1,2,3,4,5]
for i in list1:
    print(i*i)'''

list1=[1,2,3,4,5]
out=[i*i for i in list1]
print(out)

#-----------------------------------------------------------------
#create the list of 20 number from 1 to 20 using List Comprehenshion

'''number =[]     creat a emty list       }
for i in range(1,21):                     }   creat a list
    number.append(i)                      }
print(number)'''             

number=[i for i in range(1,21)]
print(number)

#----------------------------------------------------------------------
#List Comprehenshion using whuile loop
'''ist1=['h#d','beng#luru','delhi']
for i in list1:
    if '#' in i:
        print(i.replace('l','L'))'''

list1=['h#d','beng#luru','delhi']
output=[i for i in list1 if '#' in i]
print(output)

#---------------------------------------------------------------------

'''count'''
list1=[1,2,3,'a','b','c','d','d','d']
print(list1.count('b'))


#---------------------------------------------------------------------
'''Extend'''
list2=['A','B','c']
list3=[1,2,3]
list2.extend(list3)
print(list2)

'''Append vs Extend vs concat'''
#-append will add the element at last, that element can be any type 
list1=[1,2,3]
list2=['a','b']
list1.append(list2)
print(list1)

#-extend will update the list by adding new element, the result also save in a same list
list1=[1,2,3]
list2=['a','b']
list1.extend(list2)
print(list1)

#-concat will add two list, but the result will not update in same list
list1=[1,2,3]
list2=['a','b']
print(list1+list2)

#------------------------------------------------------------------------------------
#list1=['ram','hari','gopla']
#list2[20,30,40]
#output=ram age is 20

list1=['ram','hari','gopla']
list2=[20,30,40]
for i,j in zip(list1,list2):
    print("{} age is {} ".format(i,j))

#creat a normal fumction
def add (x):
    summ= x+10
    print(summ)
add(20)

#lambda function
'''syntax- Lambda<argument_name>:<output>''' #normal
'''syntax- Lambda<argument 1>,<argument2>:<output>''' #using 2 arguments
'''syntax- lambda <arg1>,<arg2>: <if_output> <if_condition> else <else_output>'''  #using if-else
'''syntax- lambda <arguments>: <output>, <iterator>''' #using for loop

add=lambda x:x+10
print(add(20))

#----------------------------------------------------------
#wap to square of a number using lambda function
square = lambda x:x*x
print(square(5))

#----------------------------------------------------------
#wap to cube of a number using lambda function
cube= lambda x:x*x*x
print(cube(2))

#----------------------------------------------------------
#wap to sum of number using lambda function
summ= lambda a,b:a+b
print(summ(20,10))

#----------------------------------------------------------
#implement avarag of 3 number using lambda
avg=lambda a,b,c:(a+b+c)/3
print(avg(10,10,10))

# make c is defult parameter
avg=lambda a,b,c=30:round((a+b+c)/3,3)
print(avg(20,30))

#----------------------------------------------------------
#creat a function for finding grater number between two number.
l1=[]
def grater(a,b):
    if a>b:
        print('a is gratrt')
        l1.append(a)
    elif a==b:
        print('a is equal b')
        l1.append(a)
        l1.append(b)
    else:
        print('b is grater')
        l1.append(b)
    print(l1)
grater(20,10)

#using list Comprehenshion
l1=[100 if 100>200 else 200]
print(l1)

#lambda
grater=lambda a,b: a if a>b else b 
print(grater(50,199))

#---------------------------------------------------------
list1=['hyd','mumbai','chennai']
#list1=['Hyd','Mumbai','Chennai']
#m-1: use append method
#m-2: use list comprhenshion

#m1
list1=['hyd','mumbai','chennai']
list2=[]
for i in list1:
    list2.append(i.capitalize())
print(list2)

#m2
output=[i.capitalize() for i in list1]
print(output)

#lambda 
list1=['hyd','mumbai','chennai']
lambda i : i.capitalize(), list1
map(lambda i : i.capitalize(), list1)
print(list(map(lambda i : i.capitalize(), list1)))

#-1st make a lambda function
#-2nd addyour iterator
#-3rd map both function iterator
#4th save the result in a list & seen the output

#------------------------------------------------------------
list1=[1,2,3,4,5]# square
lambda i: i*i, list1
map(lambda i: i*i, list1)
print(list(map(lambda i: i*i, list1)))

#------------------------------------------------------------
list1=[1,2,3]
list2=[11,12,23]  #output[12,14,26]
lambda i,j:i+j ,list1,list2
map(lambda i,j:i+j,list1,list2)
print(list(map(lambda i,j:i+j,list1,list2)))  # write this line only

#------------------------------------------------------------------
list1=['h#d','beng#luru','delhi']
print(list(filter(lambda i: '#' in i,list1)))     # if u hava using 'MAP' then gat bollan value

#------------------------------------------------------------------


#------------------------------method-1---------------------------------------------
#read the file using cord(locaton+file name+typ of file)
filepatha="C:\\Users\\SUDHANSU DAS\\OneDrive\\Attachments\\sk.txt.txt"
file=open(filepatha,encoding='utf-8-sig')
print(file.read())

#------------------------------method-2---------------------------------------------
#using 'with' 
filepatha="C:\\Users\\SUDHANSU DAS\\OneDrive\\Attachments\\sk.txt.txt"
with open (filepatha) as file:
    data=file.read()
    print(data)    #read the file
print(len(data))   #prind the length of the file

#-----------------------------------------------------------------------------------
#i went get number of lines
'''enumerate'''
for i in data:
    print(i)   #get charcters

filepatha="C:\\Users\\SUDHANSU DAS\\OneDrive\\Attachments\\sk.txt.txt"
file=open(filepatha,encoding='utf-8-sig')
for i in file:
    print(i)     #get lines

#-if you went to see lines, work on open()
#-if you went to see the charcters, work on file.read()
#-----------------------------------------------------------------------------------
#count how many lines in file

#method-1
filepatha="C:\\Users\\SUDHANSU DAS\\OneDrive\\Attachments\\sk.txt.txt"
file=open(filepatha,encoding='utf-8-sig')
count=0
for i in file:
    count+=1
print(count)   
#method-2
filepatha="C:\\Users\\SUDHANSU DAS\\OneDrive\\Attachments\\sk.txt.txt"
file=open(filepatha,encoding='utf-8-sig')
for index,line in enumerate(file):
    print(index,line)  
print(index+1)   #total line it will b count

#-----------------------------------------------------------------------------------
#Q print 1st 2 lines
filepatha="C:\\Users\\SUDHANSU DAS\\OneDrive\\Attachments\\sk.txt.txt"
file=open(filepatha,encoding='utf-8-sig')
print('hello')
for index,line in enumerate(file):
    if index<3:
        print(index,line)

string1='python'  #(*using for loop print the letter[-in,-range])

for i in string1:   #using in
    print(i,end=' ')

print("\n")


for i in range(len(string1)): #using range
    print("the index of {} is {}".format(i,string1[i]))


print(string1[-1])

print("\n")


#method-1(error is not there)
try:
    num1=10
    num2=30
    add=num1+num2
    print(add)
except Exception as e:
    print('hee')
    print(e)
    print('correct it')

#method-2(error is there)
try:
    num1=10
    num2=30
    add=num1+num244  #error is there then it will go to except.
    print(add)
except Exception as e:
    print('hee')
    print(e)
    print('correct it')

print('good byy')

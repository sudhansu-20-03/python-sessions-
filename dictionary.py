'''clear & copy'''
#take one dictionry
#take 2nd dictionrry
#copy 1st dict info 2nd
#clear 1st dict
#and print both

d1={'a':20,'b':30,'c':40,'d':50}
d2=d1.copy()
d1.clear()
print(d1)
print(d2)


#-------------------------------------------------
'''pop-popitem $ del'''

#pop will remove specify key. 
d1={'a':20,'b':30,'c':40,'d':50}
d1.pop('d')
print(d1)

#popitem remove the lastvalue default.
d1={'a':20,'b':30,'c':40,'d':50}
d1.popitem()
print(d1)

#del is a key word.
#it can delete an item by proving spicifi key.
d1={'a':20,'b':30,'c':40,'d':50}
del(d1)  #delete d1
#print(d1)

#-----------------------------------------------------
'''fromkey $ get'''
d1={'asha':20,'b':30,'c':40,'d':50}
print(d1.get('a'))

d1={'a':20,'b':30,'c':40,'d':50}
print(d1.fromkeys('asha',39))

#-----------------------------------------------------
'''set as default'''
#return value of the key, if key is not present returns defaul

t1=[(1,2),(2,3)]
d1={}

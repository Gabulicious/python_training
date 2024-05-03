mydict={
    'name':'gabriel',
    'gender':'male',
    'age':19,
    'adress':['kiambu',254,'kimathi']
}

#access values using keys
print(mydict['name'])
print(mydict['gender'])
print(mydict['age'])
#displaying 254
print(mydict['adress'][1])

#modifying values
mydict['age']=20
mydict['name']='gabu'
#adding key values to a dictionary
mydict['occupation']='economist'
mydict['id']=1020304
print(mydict)

#delete/remove
del mydict['age']
#



listVariable = range(1,20)
print("Values from 1 to 3 ",listVariable[1:3]) #get elements from 1 to 3 from starting


# extend or plust to merge the current list
listVariable = listVariable + range(21,40)
print("Merge with + other list having 20 values to ading ",listVariable)
listVariable.extend(range(40,50))
print("Extending with list using extend ",listVariable)
listVariable.insert(10,100)
print("Adding new value at 10th location ",listVariable)

# sort 
listVariable.sort();
print(" Sorted list ",listVariable)


#slices to read contineous part of list
print("Values from 1 to 3 from starting ",listVariable[1:3])
print("Values from 35 to ending ",listVariable[35:])
print("Values from starting to till 10 ",listVariable[:10])
print("Values from start to end",listVariable[:])
print("Values from last 10",listVariable[-10])

#modify, delete, lenght of list 
listVariable[1:6] = range(201,206);
print("Modify part of list from 1 to 6 values ",listVariable)
del listVariable[1:6]
print("Deleted 1 to 6 values from list", listVariable)
print("No of elements in list",len(listVariable))


#iterate over the list
for value in listVariable :
    print("Value :",value)

for index,value in enumerate(listVariable) :
    print(index,". Value:",value)
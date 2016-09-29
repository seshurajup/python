# create dictinary
dictionaryVariable = {"a":1,"b":2,"c":3}

#access dictory
print("Dictionary value for key a is ",dictionaryVariable["a"])

#modify dictory
dictionaryVariable["b"]=5
print("Modified value for key b from 3 to 5 ",dictionaryVariable["b"])

#check is index b exists in dictionaryVariable
print(" is key b exists in dictory? ",("b" in dictionaryVariable))

#delete any specific value by key()
del dictionaryVariable["b"]
print("Deleted key b value from directory ",dictionaryVariable)

#check is index b exists in dictionaryVariable
print(" is key b exists in dictory? ",("b" in dictionaryVariable))

extededDictionaryVariable = {"d":4,"e":5,"a":6}
#merge 2 dictionarys with dublicate keys 
dictionaryVariable.update(extededDictionaryVariable)
print(" what happen to key value of a after extend dictionary ",dictionaryVariable)

#iterate over dictory 
for key in dictionaryVariable :
    print(" for Key:",key," value:",dictionaryVariable[key])

for key, value in dictionaryVariable.items() :
    print(" for Key",key," value:",value)

for index, key in enumerate(dictionaryVariable.keys()) :
    print(index,". Key = ",key)

for value in dictionaryVariable.values() :
    print(" Value = ",value)





## numerical operations ##
firstVariable = 20
secondVariable = 10
thirdVariable = firstVariable + secondVariable;
print(firstVariable + secondVariable) # addition
print(firstVariable - secondVariable) # substraction 
print( firstVariable * secondVariable ) # multiplication 
print(firstVariable / secondVariable) # division
print(firstVariable % secondVariable) # modular

## string operations ##
firstVariable = "firstValue"
secondVariable = "secondValue"
thirdVariable = firstVariable + " " + secondVariable
print(firstVariable + " " + secondVariable) # concatenation
print(thirdVariable[5:10]) # slice string from 5th character to 10th characters from starting
print(thirdVariable[-11:-5]); # slice string from 5th character to 11th character from ending

## list operations ##
listVariable = ["oneValue","twoValue","thirdValue"];
print(listVariable)
print(listVariable[1]) #access 2nd value of listVariable from start
print(listVariable[-2]) #access 2nd value of listVariable from last
listVariable[2] = "fourthValue"  #change 2nd value of array
print(listVariable)
del listVariable[2] #delete 2nd value of listVariable
print(listVariable)

firstList = ["oneValue","twoValue"]
secondList = ["thirdValue","fourthValue"]
thirdList = firstList + secondList
print(thirdList) # merge multiple lists
print( len(thirdList) ) # total number of elements in list
thirdList.append("fifthValue")
print(thirdList) # added extra value 
print( thirdList.count("fourthValue")) # count no of times fourvalue repated in listVariable
#del append len count max min 

## directory operatiosn ##
directoryVariable = {"oneIndex":"oneValue", "twoIndex":"twoValue", "threeIndex":"threeValue"}
print("twoIndex Value : %s" %(directoryVariable["twoIndex"]))
del directoryVariable["twoIndex"] # delete twoIndex value from directoryVariable
print(directoryVariable)
print(directoryVariable.keys()) # all keyes in randome order ** Notebook
print(directoryVariable.values()) # all values in directoryVariable
directoryVariable2 = {"fourthIndex":"fourthValue", "fifthIndex":"fifthValue"}
directoryVariable.update(directoryVariable2) # merge 2 directory with update
print(directoryVariable)
directoryVariable.clear() # clear all values from directoryVariable
print(directoryVariable)
# del update clear keyes values


## tuples operations ##
tupleValue = ("oneValue","twoValue","threeValue")
print(tupleValue)
tupleValue = ("fourthValue","fifthValue","sixthValue")
print(tupleValue)
print(tupleValue[1]) # slice function
print(tupleValue[1:2]) # silent from 1 to 2 values from starting 
del tupleValue # delete complete variable - release memory by deleting it.

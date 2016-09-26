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
thirdList.append("fivthValue")
print(thirdList) # added extra value 
print( thirdList.count("fourthValue")) # count no of times fourvalue repated in listVariable
#del append len count max min 
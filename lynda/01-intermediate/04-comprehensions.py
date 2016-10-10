# functional progrming in pythong with comprehensions to data transform
listSquares = [value**2 for value in range(1,10)]
print(" From 1 to 10 Squares ",listSquares)

# adding filters for list
listEvenSquares = [value**2 for value in range(1,10) if value % 2 == 0]
print(" From to 10 event Squares ",listEvenSquares)

# adding filter for dictionary 
dictionaryEvenSquares = {key:key**2 for key in range(1,10) if key % 2 == 0}
print(" From 1 to 10 even Squares with its value",dictionaryEvenSquares)

# add value i*5 to all Values
listValues = range(1,10)
list5Values = [value*5 for value in listValues]
print(" multiple 5 to each value of range 1 to 10 ",list5Values)
print(" sum of all values of list5Values ",sum(list5Values))
print(" Short form of writing sum without creating extra list",sum(value*5 for value in listValues))

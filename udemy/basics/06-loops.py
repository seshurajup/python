## for loop ##
for i in range(1,10,2) :
    print(" Values of i is %d" % (i))

arrayVariable = ["oneValue","twoValue","threeValue"]
for value in arrayVariable :
    print(" array value %s" % (value))

tupleVariable = ("oneConstant","twoConstant","threeConstant")
for constant in tupleVariable :
    print(' tuple value %s' % (constant))

## while loop ##
indexVariable = 1;
while indexVariable < 5 :
    print(indexVariable)
    indexVariable = indexVariable + 1;

## loop control statements continue, break, pass ##
indexVariable = 0;
while indexVariable < 100 :
    indexVariable += 1
    if indexVariable == 10 :
        break
    elif indexVariable == 5 :
        continue
    else :
        pass
    print(indexVariable)
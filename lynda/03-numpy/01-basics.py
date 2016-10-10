import numpy as np 
import matplotlib.pyplot as mpl


numpyVariable = np.array([1,2,3,4,5])
print("numpy array :",numpyVariable)

numpyFloatVariable = np.array([1,2,3,4,5],dtype=np.float64)
print("numpy array :",numpyFloatVariable)
print("Total dimentions: ",numpyFloatVariable.ndim )
print("Shape of variable: ",numpyFloatVariable.shape )
print("Size of variable: ",numpyFloatVariable.size )

numpyMultiDimentionalVariable = np.array([[1,2,3,4,5],[1,2,3,4,5]],'d')
print("Multi Dimentional array",numpyMultiDimentionalVariable);
print("Total dimentions: ",numpyMultiDimentionalVariable.ndim )
print("Shape of variable: ",numpyMultiDimentionalVariable.shape )
print("Size of variable: ",numpyMultiDimentionalVariable.size )

print(" Zero 3x2 array ",np.zeros((3,2),"d"));
print(" Empty almost zero 3x2 array ",np.empty((3,2),"d"));
print(" 5 points from 0 to 10 ",np.linspace(0,10,5));
print(" 5 range points from 0 to 10 ",np.arange(0,10,2));
print(" random numbers of 3x2 array ",np.random.standard_normal((3,2)))


firstArray = np.random.standard_normal((3,2))
secondArray = np.random.standard_normal((3,2))

mergeArray = np.hstack([firstArray, secondArray]);
print(" Join 2 arrays horizontally",mergeArray)
mergeArray = np.vstack([firstArray,secondArray]);
print(" Join 2 arrays vertically",mergeArray)
print(" Transpose array ",np.transpose(mergeArray))

np.save("mergeArray.npy",mergeArray)
loadArray = np.load("mergeArray.npy")
print(" Loaded array:",loadArray)








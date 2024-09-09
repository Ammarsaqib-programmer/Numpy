import numpy as np
array_A = np.array([[1,2,3],[4,5,6]])
print(array_A.size)
array_b=array_A.reshape(1,6)
print(array_b)

#Transpose
array_b=array_A.T
print(array_b)

#to print specific column
print(array_b[0])
print(array_b[:,1])
print(array_b[0,0])
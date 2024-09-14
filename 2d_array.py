import numpy as np
var1 = np.array([[1,2,3,4],[5,6,7,8]])
var2 = np.array([[8,7,6,5],[4,3,2,1]])
print("first array",var1,"\n")
print("secomd array",var2,"\n")
varadd= var1 + var2
varadd1= var1 - var2
varadd2= var1 * var2
varadd3= var1 / var2
print("The answer of sum is :\n",varadd)
print("The answer of subtraction is :\n",varadd1)
print("The answer of multiplication is :\n",varadd2)
print("The answer of division is :\n",varadd3)
varad = np.reciprocal(var1)
print(varad)

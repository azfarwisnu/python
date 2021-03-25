import numpy as np 

'''
a = np.array([1, 2 ,3])
b = np.array([[2, 5, 7],[3, 9, 8]], dtype = complex)
c = np.array([[2, 5, 7],[3, 9, 8]])
print(a)
print("==============")
print("with complex \n",b)
print("===============")
print("no complex \n",c)
'''
a = np.array([[2, 5],[3, 1]])
b = np.array([[3, 2],[4, 3]])

c = a + b
print(c)

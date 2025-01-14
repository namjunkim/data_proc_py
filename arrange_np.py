import numpy as np

array = np.array([5, 9, 10, 3, 1])
array.sort()
print(array[::-1]) #index desc

array = np.array([[5, 9, 10, 3, 1], [8,4,3,2,5]])
array.sort(axis=0)
print(array)

array = np.linspace(0, 10, 5) #even spacing
print(array)

#random
np.random.seed(7) #same random num
print(np.random.randint(0,10,(2,3)))

#np reference change
array1 = np.arange(0, 10)
array2 = array1
array2[0] = 99
print(array1)
#np copy
array1 = np.arange(0, 10)
array2 = array1.copy()
array2[0] = 99
print(array1)

#remove dupilcation
array = np.array([1,1,1,4,5,6,6,9])
print(np.unique(array))


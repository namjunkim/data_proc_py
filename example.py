
import numpy as np

#list_data = [1, 2, 3]
#array = np.array(list_data)

#print(array.size)
#print(array.dtype)
#print(array[2])


# to make array from 0 to 3
array1 = np.arange(4)

print(array1)

array2  = np.zeros((4,4), dtype=float)
print(array2)

array3 = np.ones((3,3), dtype=str)
print(array3)

# to make random range 0 to 9
array4 = np.random.randint(0,10, (3,3))
print(array4)

# to make array, average 0, and std 1
array5 = np.random.normal(0,1,(3,3))
print(array5)

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.concat([arr1,arr2])
print(arr3.shape)
print(arr3)

a1 = np.array([1,2,3,4])
a2 = a1.reshape((2,2))

print(a2)


array1 = np.arange(4).reshape(1,4)
array2 = np.arange(8).reshape(2,4)

print(array2)

array3 = np.concat([array1, array2], axis=0)
print(array3)

array = np.arange(8).reshape(2,4)
left, right = np.split(array, [2], axis=1) #axix=1는 열
print(left.shape)
print(right.shape)
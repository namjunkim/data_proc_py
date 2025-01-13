import numpy as np

array = np.random.randint(1, 10, size=4).reshape(2,2)
print(array)

result_array = array * 10
print(result_array)

array1 = np.arange(4).reshape(2,2)
array2 = np.arange(2)

array3 = array1 + array2
print(array3)

array1 = np.arange(0, 8).reshape(2,4)
array2 = np.arange(0,8).reshape(2,4)
array3 = np.concatenate([array1, array2], axis=0)

array4  = np.arange(0,4).reshape(4,1)

print(array3 + array4)

#masking
array1 = np.arange(16).reshape(4,4)
print(array1)

array2 = array1 < 10
print(array2)

array1[array2] = 100
print(array1)

#sum
array = np.arange(16).reshape(4,4)
print("max : ", np.max(array))
print("mim : ", np.min(array))
print("sum : ", np.sum(array))
print("mean : ", np.mean(array))

print("sum(0) : ", np.sum(array, axis=0))
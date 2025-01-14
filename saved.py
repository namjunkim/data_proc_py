import numpy as np

array1 = np.arange(0,10)
array2 = np.arange(10,20)

np.savez('saved.npz', array1=array1, array2=array2)

data = np.load('saved.npz')
result1 = data['array1']
result2 = data['array2']
print(result1)
print(result2)
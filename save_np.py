import numpy as np

array = np.arange(0, 10)
np.save('saved.npy', array)

result = np.load('saved.npy')
print(result)
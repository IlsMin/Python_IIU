import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]], float)
# >>>
print(a[1,:])
# array([ 4.,  5.,  6.])
# >>> 
print(a[:,2])
# array([ 3.,  6.])
# >>> 
print(a[-1:, -2:])
# array([[ 5.,  6.]])
https://colab.research.google.com/drive/1Uqgy6zBmdjmM7VEegImVVyWq3hOnaAxm?usp=sharing
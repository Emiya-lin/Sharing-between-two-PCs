# 3 + 'abc' is error expression.
str(3) + 'abc' # legal expression - type conversion

'a' > 3 # what's going to happen? 



# Usage of list
l1 = [1, 2, 3, 4, 5]
print("l1: ", l1, "type of l1: ", type(l1))
l2 = [6, 7]
print("l1+l2: ", l1+l2) # [1, 2, 3, 4, 5, 6, 7]
l3 = [3, 7]
print("l1+l3: ", l1+l3) # [1, 2, 3, 4, 5, 3, 7]

l4 = ['Lee', 1865, 'Robert'] # multiple types confusion
print("Type of l4(multi-type elements): ", type(l4[0]), type(l4[1]))
print("the length of l4:", len(l4))


# 创建连续的整数数组
intgList = range(9, 23) # range(head, tail+1) for list [head, head+1, head+2, ..., tail]
for i in range(len(intgList)):
    print(intgList[i])



# vector in python
# list for python vs. np.array-vector in numpy
import numpy as np
l5 = np.array(l1)
print(l5, "type of l5: ", type(l5))

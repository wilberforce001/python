import numpy as np

a = [1, 2, 3, 4, 5]
print(type(a))

b = (1, 2, 3, 4, 5)
print(type(b))

c = np.array(b)
print(type(c))

#CALCULATING AREA

length_dim = [1.1, 20.5, 53.6, 26.7, 89.4] #length in metres
width = [10.23, 28.15, 24.6, 33.58, 54] #width in metres

#OPTION 1
area = [] #Initialize empty list
for i in range(len(length_dim)): # Assumes lists of equal length
    l = length_dim[i]
    w = width[i]
    area.append(l * w)
print("Area: ", area)

#OPTION 2
area = [length_dim[i] * width[i] for i in range(len(length_dim))] #Assumes lists of equal length
print("Area: ", area)

#OPTION 3
area = []
for l, w in zip(length_dim, width): #Lists can be of different lengths
    area.append(l * w)
print("Area: ", area)

import numpy as np
np_length = np.array(length_dim)
np_width = np.array(width)

area = np_length * np_width

print(area)

#Adding lists
length_dim = [1.1, 20.5, 53.6, 26.7, 89.4] #length in metres
width = [10.23, 28.15, 24.6, 33.58, 54] #width in metres

sum_dim = length_dim + width
print(sum_dim) #Append the 2 lists together, list is now longer

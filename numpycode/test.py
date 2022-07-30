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

#Example 1
# Adding 2 lists
length_dim = [1.1, 20.5, 53.6, 26.7, 89.4] #length in metres
width = [10.23, 28.15, 24.6, 33.58, 54] #width in metres

sum_dim = length_dim + width
print(sum_dim) #Append the 2 lists together, list is now longer

#Example 2
import numpy as np 
sum_dim = np.array(length_dim) + np.array(width)
print(sum_dim)

#Convert length in meters to centimeters
length_dim = [1.1, 20.5, 53.6, 26.7, 89.4] #length in metres
length_cm = [l * 100 for l in length_dim]
print(length_cm)

#Revisit
import numpy as np
np_length = np.array(length_dim)
np_length_cm = np_length * 100
print(np_length_cm)

#Numpy can perform multiplication on more than 1000 measurements
#d = np.empty(1000, int) # can specify the datatype
#print(d, "\n")
#product = d * 2
#print(product)


#Generating arrays with random values
a = np.zeros(3, int) #Arrays with zeros
print(a)

b = np.ones(5, str)
print(b)

c =np.empty(10, int)
print(c)

e = np.arange(15) #(start, stop, step)
print(e)

f =np.random.randint(5, size = (2,4))
print(f)
# Program to claculate BMI

name1 = "John"
height1 = 22
weight1 = 33

name2 = "Steve"
height2 = 12
weight2 = 10

name3 = "Paul"
height3 = 40
weight3 = 11

name4 = "Caleb"
height4 = 35
weight4 = 14

#BMI CALCULATOR
def bmi_calculator(name, height, weight):
    bmi = weight / (height ** 2)
    print("bmi: ") 
    print(bmi)
    if bmi < 25:
        return name + (" is not overweight")
    else: 
        return name + (" is overweight")

result1 = bmi_calculator(name1, height1, weight1)
result2 = bmi_calculator(name2, height2, weight2)
result3= bmi_calculator(name3, height3, weight3)
result4 = bmi_calculator(name4, height4, weight4)

print(result1)
print(result2)
print(result3)
print(result4)



#Numpy array

from unicodedata import name
import numpy as np
name_john = np.array(name1)
height_john = np.array(height1)
weight_john = np.array(weight1)

bmi = weight_john / (height_john ** 2)

print(bmi)

name_steve = np.array(name2)
height_steve = np.array(height2)
weight_steve = np.array(weight2)

bmi = weight_steve/ (height_steve ** 2)

print(bmi)

name_paul = np.array(name3)
height_paul = np.array(height3)
weight_paul = np.array(weight3)

bmi = weight_paul / (height_paul ** 2)

print(bmi)

name_caleb = np.array(name4)
height_caleb = np.array(height4)
weight_caleb = np.array(weight4)

bmi = weight_caleb/ (height_caleb ** 2)

print(bmi)


#Checking time for Execution

import time 
start = time.time()

def bmi_calculator(name, height, weight): #LISTS
    bmi = weight / (height ** 2)
    print("bmi: ") 
    print(bmi)
    if bmi < 25:
        return name + (" is not overweight")
    else: 
        return name + (" is overweight")

end = time.time()
print("The time of execution of above List program is :", end-start)


import time 
start = time.time()

def bmi_calculator(name, height, weight): #NUMPY ARRAYS
    bmi = weight_john / (height_john ** 2)
    bmi = weight_steve/ (height_steve ** 2)
    bmi = weight_paul / (height_paul ** 2)
    bmi = weight_caleb/ (height_caleb ** 2)
print(bmi)

end = time.time()
print("The time of execution of above Numpy program is :", end-start)

#TIME DIFFERENCE 
elapsed_time = end - start
print('Execution time:', elapsed_time, 'seconds')







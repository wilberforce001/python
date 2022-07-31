#Example 1
from sqlite3.dbapi2 import _Statement
import time

start = time.time()

a = 0
for i in range (1000):
    a += (i**100 )

end = time.time()

print("The time of execution of above progrom is :", end-start)

#Example 2
import time

for j in range(100, 1100, 100):
    start = time.time()

    a = 0
    for i in range(j):
        a += (i**100)

end = time.time()

print("Time for execution of program for {} order of computations: {}". format(j, round(end-start, 10)))

#Method 2
from datetime import datetime

start = datetime.now()

a = 0
for i in range(1000):
    a += (i**100)

end = datetime.now()

print("The time of execution of above program is :", str(end-start)[5:])


#Example 3
import time

st = time.time()

sum_x = 0
for i in range(1000000):
    sum_x += i

time.sleep(3)
print('Sum of first 1 million numbers is:', sum_x)

et = time.time()

elapsed_time = et -st
print('Execution time:', elapsed_time, 'seconds')


#Time taken for the program to execute
import time

start = time.time()

for i in range(10):
    print(i)

time.sleep(1)

end = time.time()

print(f"Runtime of the program is {end - start}")

#TIME DIFFERENCE 
elapsed_time = end - start
print('Execution time:', elapsed_time, 'seconds')

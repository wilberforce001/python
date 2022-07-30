import numpy as np
import time
size_of_vec = 1000000

def pure_python_version():
    start = time.time()
    X = range(size_of_vec) # X = [0, 1, 2, 3, ...., 999999]
    Y = range(size_of_vec) # Y = [0, 1, 2, 3, ...., 999999]
    Z = [X(i) + Y(i) for i in range(len(X))]
    return time.time() - start
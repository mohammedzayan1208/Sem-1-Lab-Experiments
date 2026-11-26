# Experiment 16: Create, append, and remove elements using NumPy
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print("Original array:", arr)

arr = np.append(arr, [60, 70])
print("Array after appending elements:", arr)

arr = np.delete(arr, 2)
print("Array after removing element at index 2:", arr)

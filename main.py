import random
import numpy as np

# Generate 1000 ramdom number between 1 and 100
num = 1000
randomNumbers = [0]*num
for i in range(num):
	randomNumbers[i] = random.randint(1,101)

# Compute std and var
std = np.std(randomNumbers)
var = np.var(randomNumbers)
print('std: %f, var; %f'% (std, var))
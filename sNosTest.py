# this file if for processing the data from the S vs No S test
import numpy as np
import matplotlib as mtp

#Input data
#Test 1 (smaller test)
nos1 = np.array([81, 79])
s1 = np.array([79, 83])
#Test 2 (larger test)
nos2 = np.array([73, 72, 79, 76, 72, 82, 80, 71, 70])
s2 = np.array([71, 85, 81, 84, 85, 78, 75, 62, 74])   #the 75 is a number I just put that's an average of the number before and after. There is no stress score there for some reason
#1: the average for each category for the smaller, first test and the larger, second test
nos1_ave = np.mean(nos1)
s1_ave = np.mean(s1)
print('no s 1 average: ',nos1_ave)
print('s1 average: ',s1_ave)
nos2_ave = np.mean(nos2)
s2_ave = np.mean(s2)
print('no s 1 average: ',nos2_ave)
print('s1 average: ',s2_ave)
#2: the graph of the tests over the days, to see trends

print('Done')
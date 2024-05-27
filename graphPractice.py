# this file is for learning about graphing. How to make it look nice, how to have different figures, and how to present information in different ways
import matplotlib as plt
import numpy as np
#from matplotlib import pyplot as pyp

# try to figure out the figures
x = np.arange(0,5*np.pi,.1)
y = np.sin(x)
y2 = np.cos(x)
pyp.figure(1)
pyp.plot(x,y)
pyp.show()

pyp.figure(2)
pyp.plot(x,y2)
pyp.show()

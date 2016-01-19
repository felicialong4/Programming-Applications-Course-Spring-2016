import numpy as np
from numpy import sin, cos, pi
import matplotlib.pyplot as plt
plt.gca().set_color_cycle(['blue', 'red'])
a = np.linspace(0, 6*pi, pi/2)
sin_graph = sin(a)
cos_graph = cos(a)
 
plt.plot(a, sin_graph)
plt.plot(a, cos_graph)
plt.ylabel("y")
plt.xlabel("x")
plt.legend(('sin(x)', 'cos(x)'))

x = np.linspace(0, 6*pi, 100)
line, = plt.plot(x, np.sin(x), '--', linewidth=2)
line0 = plt.plot(x, np.cos(x), linewidth=2)
dashes = [10, 5, 100, 5]
line.set_dashes(dashes)
plt.show()
#import numpy and matlibplots module


#generate array of x values from 0 to 6pi

#calculate y values for sin wave

#calculate y values for cosine wave

#plot x and y values for both functions 

#set dashed line for sine wave and solide line for cosine wave

#add legend


#leave comment here with your information
#Name:Felicia Long
#Date:1/19/15


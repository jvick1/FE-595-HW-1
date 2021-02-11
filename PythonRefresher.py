import matplotlib.pyplot as plt 
import numpy as np 

#one period of sine and cosine is 2pi 
#define a set "plot_range" starting at 0 to 2pi with increments of 0.1 so it's smoother
plot_range = np.arange(0,2*np.pi,0.1)

#sine and cosine functions with plot_range as the input
Sine = np.sin(plot_range)
Cosine = np.cos(plot_range)

#plot
plt.plot(plot_range, Sine, plot_range, Cosine)
plt.xlabel("0 to 2pi")
plt.ylabel("Sine and Cosine")
plt.title("Sine and Cosine 1 Period Plot")
plt.legend(["Sine", "Cosine"])
plt.show()

# Tangent function
#Tangent = np.tan(plot_range)
#plot
#plt.plot(plot_range, Sine, plot_range, Cosine, plot_range, Tangent)
#plt.xlabel("0 to 2pi")
#plt.ylabel("Sine, Cosine and Tangent")
#plt.title("Sine, Cosine and Tangent 1 Period Plot")
#plt.legend(["Sine", "Cosine", "Tangent"])
#plt.show()

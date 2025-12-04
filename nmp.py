import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data=np.array([1,2,3,4,5])
# print(data)
# print(type(data))
# print(len(data))
# print(data.shape)

# s=pd.Series(data)
# print(s)

xpoints = np.array([0,3,5,7,9])
ypoints = np.array([0,1,4,9,16])    

plt.plot(xpoints, ypoints)
# plt.plot(xpoints, ypoints,  'o')
# plt.show()
plt.savefig("plot.jpg")
print("Plot saved as plot.jpg")

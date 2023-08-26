import matplotlib.pyplot as plt 
import numpy as np 
phone_names=['apple','one-plus','google','lava']
sales_world=np.array([25,34,12,54])
xp=[0,0.10,0,0.21]
# creating pie chart
plt.pie(sales_world,autopct='%1.1f%%',labels=phone_names,explode=xp,shadow=True)
plt.show()


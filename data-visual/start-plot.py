import matplotlib.pyplot as plt 

# creating dataset
x=[3,8,5,15]
x1=[4,9,6,16]
y=[5,13,7,21]
y1=[4,12,6,20]
# creating x-axis
plt.xlabel('x')
plt.ylabel('y')
plt.title('bachpan ki yaden')
plt.scatter(x,y,marker='*',s=120,label='water')
plt.scatter(x1,y1,marker='^',s=220,label="soil")
# draw lines
plt.plot(x,y)
plt.plot(x1,y1)
# bar plot 
plt.bar(x,y)
plt.bar(x1,y1)
plt.legend(loc=4) # to show labels of scatter
plt.grid() 
plt.show()
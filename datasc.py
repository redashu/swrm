import matplotlib.pyplot  as plt
x=[5,3,9]
y=[12,15,10]
plt.xlabel('distance')
plt.ylabel('time')
plt.grid(c='green')
plt.scatter(x,y,label="stations")  #  this will plot a line 
plt.plot(x,y,label="railway track")
plt.bar(x,y)
plt.legend()  # it will display label in  plots 
plt.show()   #  to  show the graph 

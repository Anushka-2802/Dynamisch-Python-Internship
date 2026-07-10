'''
Matplotlib is a Python library used for creating graphs and visualizations 
such as line charts, bar charts, pie charts, scatter plots, and histograms
'''
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8]
y=[10,12,14,16,18,20,22,24]
plt.plot(x,y)
plt.show()

#Bar chart used to comparing categories
plt.bar(x,y)
plt.show()

#Line plot used to showing trends overtime
months = ["Jan","Feb","Mar","Apr","May"]
sales = [100,120,140,130,170]
plt.plot(x,y,
         color="r",
         marker="o",
         linestyle="--",
         label="sales"
         )
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Line Plot")
plt.show()


#Scatter plot:used for finding relationships between two variables
height = [150,155,160,165,170]
weight = [45,50,55,60,68]

plt.scatter(height, weight)
plt.title("Height vs Weight")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()

#Histogram showing frequency distribution
marks = [55,60,65,70,75,80,82,85,88,90,95]
plt.hist(marks)
plt.title("Marks Distribution")
plt.show()


#Pie chart showing percentage distribution
subjects = ["Python","Java","C++","SQL"]
students = [35,25,20,20]

plt.pie(
    students,
    labels=subjects,
    autopct="%1.1f%%"
)

plt.title("Students by Subject")
plt.show()
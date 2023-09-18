import numpy as np
import matplotlib
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight') ##style used for graph

#this section of the code takes in two data sets as inputs and plots them against
# one another. plt is the module that graphs the inputs. xlabel and ylabel refer to the labels
# shown on the x and y axis. title command refers to the title of the graph. without
# plt.show() command the graph would not be displayed on screen. legend is used to
# differentiate which data refers to which graph and label indicates the data.

weekDays = [1,2,3,4,5]
salesOnWeekDays = [100,382,748,323,333]
plt.bar(weekDays, salesOnWeekDays, label="Weekday") #bar for bar chart
plt.xlabel('Day')
plt.ylabel('Sales(£)')
plt.title('Restaurant sales in £ in a week')

weekendsDays = [6, 7]
salesOnWeekends = [1000,1376]
plt.plot(weekendsDays, salesOnWeekends, marker ='.',label="Weekends") ##plot uses a line plot, bar uses a bar chart method
plt.legend()

plt.show()

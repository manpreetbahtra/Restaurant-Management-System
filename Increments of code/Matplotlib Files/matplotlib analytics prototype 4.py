import csv
from collections import Counter 
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt

#counter is a built in class in python that counts how many times an
#item has appeared in a list.

plt.style.use('fivethirtyeight') ##style used for graph

#this section of the code takes in two data sets as inputs and plots them against
# one another. plt is the module that graphs the inputs. xlabel and ylabel refer to the labels
# shown on the x and y axis. title command refers to the title of the graph. without
# plt.show() command the graph would not be displayed on screen. legend is used to
# differentiate which data refers to which graph and label indicates the data.

##weekDays = [1,2,3,4,5]
##salesOnWeekDays = [100,382,748,323,333]
##plt.bar(weekDays, salesOnWeekDays, label="Weekday") #bar for bar chart
##plt.xlabel('Day')
##plt.ylabel('Sales(£)')
##plt.title('Restaurant sales in £ in a week')
##
##weekendsDays = [6, 7]
##salesOnWeekends = [1000,1376]
##plt.plot(weekendsDays, salesOnWeekends, marker ='.',label="Weekends") ##plot uses a line plot, bar uses a bar chart method
##plt.legend()
##
##plt.show()

##################staff late matplotlib############
##here it is opening the file and analysing the number of times the staff member's name is mentioned to analyse the number
#of times they were late. 

with open('staffLate.txt') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    lateCounter = Counter()

    for row in csv_reader:
        lateCounter.update(row['staffLate'].split(';'))

        
staff = []
numberOfLates =[]
   
##print(lateCounter)
for item in lateCounter.most_common(11):#print(lateCounter.most_common(1)) returns the staff with most number of lates
    staff.append(item[0])# this line retrieves the staff name based on the most lates.
                   #index 0 as staff name is before their no. of lates in the tuple that lateCounter prints/gets.
    numberOfLates.append(item[1]) #at index 1 is the number of lates in tuple
    
print(staff)
print(numberOfLates)


plt.bar(staff, numberOfLates)
plt.xlabel('Staff Member')
plt.ylabel('Number of lates')
plt.title('Number of times a staff member is late this week')
plt.show()



###########top ten items sold#################
##here it is opening the file and analysing the number of items the item was purchased. 
with open('itemsSold.txt') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    tenbestSellingItemsCounter = Counter()

##    row = next(csv_reader)
##    print(row['itemsSold'].split(';'))#this retrieves the list of languages but only from a single row.
    

    for row in csv_reader: #this retrieves the list of languages from all rows.
        tenbestSellingItemsCounter.update(row['itemsSold'].split(';'))

bestSellingItems = []
numberOfTimesSold =[]
        
for item in tenbestSellingItemsCounter.most_common(11):
    bestSellingItems.append(item[0])
    numberOfTimesSold.append(item[1])

print(bestSellingItems)
print(numberOfTimesSold)

plt.bar(bestSellingItems, numberOfTimesSold)
plt.xlabel('Menu Items')
plt.ylabel('Number of times Bought')
plt.title('Top ten best selling items of the restaurant')
plt.tight_layout()
plt.show()

##for x in tenbestSellingItemsCounter.most_common(10):#print(lateCounter.most_common(1)) returns the staff with most number of lates
##    bestSellingItems.append(x[0])# this line retrieves the staff name based on the most lates.
##                   #index 0 as staff name is before their no. of lates in the tuple that lateCounter prints/gets.
##    numberOfTimesBought.append(x[1]) #at index 1 is the number of lates in tuple
##    

##THIS PROTOTYPE MAINLY FOCUSES ON VERTICAL BAR CHART OBTAINED FROM GRAPHING TEN MOST POPULAR MENU ITEMS.
## AS THE GRAPH LABELS ON X AXIS ARE OVER CROWDED/ THE NAMES ARE NOT DISPLAYED PROPERLY, I HAVE DECIDED TO IMPLEMENT IT AS
##HORIZONTAL BAR CHART IN THE NEXT PROTOTYPE. 

##work through the video and finish coding by today


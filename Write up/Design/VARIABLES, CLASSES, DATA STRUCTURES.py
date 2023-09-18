key variables, data structures and classes

username
password
confirm password

variables in menu- price of item, subtotal, tax and total is dependent on the item.
subtotal comprises of the price of all items in receipt. 20% of the items price is added to tax each
item an added to receipt. 

product code, item name, quantity and reorder level are variables in inventory. these are taken as inputs
from the user, hence need to be validated. product code can only be integers and is limited to 4 characters.
item name is restricted to strings with length of maximum 14 characters. quantity and reorder level are
restricted to integers only. 


variables for staff- fullname- validated to a maximum of 30 characters.
address- validated to a maximum of 30 characters and implemented as string
phonenumber - implemented as string - max of 15 characters
hoursWorked- max 4 characters and float data type
ratePerHour - float and 5 characters max
tax -float and 4 characters max
grossPayment netPay-  - float and 7 characters max

data structures

login details stored as records after succesful registration

items in menu receipt are stored as array- they are of same data type- string. they are mutable meaning
they can be changed while the program is running. their quantity can be changed and
can be deleted or added to the receipt while the program is being executed. they are then
stored in a database(e.g. as MYSQL or text file) where they are later analysed in
analytics module to determine most sold items. 

static list can be used for storing the toppings in pizza module. this is because
max number of toppings is fixed. elements can be deleted and added to a list.


inventory products are stored in a dictionary to store the data values in key and value pairs. product code
is unique, thus can be used as key and item name, quantity and reorder level values.

paylsip- texxt file all inputs are stored in a database( for e.g. as tuples/records) 

FROM STAFF INFO 
classes
POS- for menu module. this is because all the data and functionality
of the menu system is bundled together (encapsulation). class can be
called in the future and code can be reused.

inventory- gui and functions can be stored inside the same class. if any bugs are found, it would only
affect the specific class and not the whole system.

staff - implemented as class. allows it to encapsulate the data and functionality. 

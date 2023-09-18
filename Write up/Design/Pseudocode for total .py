subtotal = 0
tax = 0
total = 0
menuItemsSelection = ['a', 'b', 'c']
for x = 0 to len(menuItemsSelection) - 1 
    input price
    subtotal = subtotal + price
    tax = tax + (price / 10)
    total = subtotal + tax
next x
output "Total bill :" + total

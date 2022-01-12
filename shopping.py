shopping_list = ['shirts','pants','eggs','pasta','rice','bread']

# for itemt in shopping_list: # items is not a python function, any text can be within for '...' in
#     if itemt != 'eggs': # Removes item not within the shopping list
#         print("I need to buy " + itemt)

for itemt in shopping_list:
    if itemt == 'eggs':
      #  continue # if above is within loop, it continues over the step and finishes the statement
        break # if above is within loop, it breaks the rest of the statement off
    print("I need to buy " + itemt)




'''	_str_(function)
	append(function)
	count(function)
	extend(function)
	sort(function)
	title(function)
	remove(function)
'''

groceries = []


# 1. function to add shopping_list
def add_to_list(item): # This tells the function "I'm going to feed you an 'item' later, just trust me it exists"
	item = item.lower()
	if  item in groceries:#if item is in the grocery list:
		return "You already have this item in your list." # instructions said return, but later said display-- which is it?
	groceries.append(item)
	for i in alphabetize():
		print i.title()


# 2 function that returns the shopping list in alphabetical order:
def alphabetize():
	groceries.sort()
	return groceries


#3 function to remove an item from list:

def remove_item(item):
	item = item.lower()
	if item not in groceries: #if item is in the grocery list:
		print("You do not have this item in your list.")
	else: 
		groceries.remove(item) # remove item
		for i in alphabetize():
			print i.title()

#4 Test with the following
print "--"
add_to_list("fig")
print "--"
add_to_list("orange")
print "--"
add_to_list("fertilizer")
print "--"
add_to_list("peanuts")	
# add something already on the list
print "--"
add_to_list("peanuts")	

# remove something
print "--"
remove_item("fig")

# remove something not on the list
print "--"
remove_item("tulip")





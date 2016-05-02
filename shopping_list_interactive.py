


groceries = []


'''	_str_(function)
	append(function)
	count(function)
	extend(function)
	sort(function)
	title(function)
	remove(function)
'''

def main():
	Item_to_add=""
	
	# for item in range(0,100): # Makes a range, and then loops over it, starting at 0 and ending after 9. 
 							   # Stores the number in the variable 'item', which we could have named anything.

	while Item_to_add != "x": # while loop means "do this until the condition is false"
		Item_to_add = raw_input("Enter your Grocery items, Type X when done.   ").lower()
		if Item_to_add == "x":
			print("you are done")
		else:
			add_item(Item_to_add)

	print("Now remove items from the list. Press X to finish.")
	Item_to_remove = ""
	while Item_to_remove != "x": #while loop-"do this until false"

		Item_to_remove = raw_input("Enter the Grocery you would like to remove, Type X when done.   ").lower()

		if Item_to_remove == "x":
			print "All done."
		else:
			remove_item(Item_to_remove)
	   

def print_list():
	print ("Shopping list")
	for item in groceries:
		print item.title() #Capitalizes firt letter, l/c following.


def add_item(Item_to_add):
	if Item_to_add in groceries:#if item is in the grocery list:
		print("You already have this item on your list.") 
		should_remove = raw_input("Would you like to remove it? (yes or no) ").lower()#change answer to l/c
		if should_remove == "yes": 
			groceries.remove(Item_to_add) # remove item
			should_remove = raw_input("would you like to remove another item? (yes or no")
			if should_remove == "yes":
				bubblebutt = raw_input("What item? ").lower()
				groceries.remove(bubblebutt)  # remove more items

		else:
			print (Item_to_add)

		# ask if they want to remove, then call remove_item(Item_to_add)
 	else:
 		groceries.append(Item_to_add)
		groceries.sort()
 		print_list()

def remove_item(Item_to_remove):# 
	if Item_to_remove not in groceries:
		print("You do not have this item on your list.")  
 	else:
 		groceries.remove(Item_to_remove)
 		print_list()


groceries.sort
main()


	





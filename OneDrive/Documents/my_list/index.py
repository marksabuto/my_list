print("Script started")  # Debug statement
my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("My List:", my_list)  # Output: My List: [10, 20, 30, 40] 
print("Script finished")   # Debug statement

# Insert 15 at the second position (index 1)
my_list.insert(1, 15)

# Print the updated list
print("Updated List:", my_list)  # Output: Updated List: [10, 15, 20, 30, 40]   

# List to be added
new_elements = [50, 60, 70]

# Extend my_list with new_elements
my_list.extend(new_elements)

# Print the updated list
print("Extended List:", my_list)  # Output: Extended List: [10, 15, 20, 30, 40, 50, 60, 70] 

# Original list
my_list = [10, 15, 20, 30, 40, 50, 60, 70]

# Remove the last element
my_list.pop()

# Print the updated list
print("Updated List:", my_list)  # Output: Updated List: [10, 15, 20, 30, 40, 50, 60]

# Original list
my_list = [10, 15, 20, 30, 40, 50, 60]

# Sort the list in ascending order
my_list.sort()

# Print the sorted list
print("Sorted List (Ascending):", my_list)  # Output: Sorted List (Ascending): [10, 15, 20, 30, 40, 50, 60] 

# Original list
my_list = [10, 15, 20, 30, 40, 50, 60]

# Find the index of the value 30
index_of_30 = my_list.index(30)

# Print the index
print("Index of 30:", index_of_30)  # Output: Index of 30: 3
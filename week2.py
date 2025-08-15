# Creating my empty list
my_list = []

# appending elemnts to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# inserting an element at index 1 which is 15
my_list.insert(1, 15)

# extending the list with multiple elements which are 50, 60, and 70
my_list.extend([50, 60, 70])

# removing the last element from the list which is 70
my_list.pop()

# sorting my list in ascending order
my_list.sort()

# finding the index of the element 30 in the list and printing it
index_30 = my_list.index(30)
print("List after all operations:", my_list)
print("Index of 30:", index_30)

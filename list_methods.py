friends = ["Apple", "Banana", "Cherry", 4, 2, 3, True, False, "Aakash", "Arun"]

print(friends[8])

friends.append("Sagar") # append = add an item to the end of the list
print(friends)

l1 = [1, 3, 7, 2, 5, 4]
# l1.sort() # sort = sorts the list in ascending order


l1.insert(2, 9) # insert = inserts an item at the given index
print(l1)
l1.sort()
print(l1)

print(l1.pop(3))
value = l1.pop(3)
print(value)# print a riturn value of pop

list = [1, 2, 3, 4, 5, 1, 6, 7, 8, 1]
list.remove(1) # remove = removes the first occurrence of the given item
print(list)

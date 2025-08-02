# #List declaration and retrieving elements of a list.
# student = [10, 'aditya', 'Male', 26, 'May', 1990]
# print(student)
# print(student[0])
# print(student[1: ])

# #Program to create lists using range()
# list1 = range(10)
# print('--' * 2)
# for i in list1:
#     print(i)
#     print("End of iteration: ", i+1)
#     print('--' * 5)
# print("THE END")

# #Program to access list elements using loops
# lst = [10, 20, 30, 40, 50]
# print("Using for Loop: ")
# for i in lst:
#     print(i)
# print("End of for Loop.")
# print()

# lst = [10, 20, 30, 40, 50]
# print("Using while Loop:")
# i = 0
# while i < len(lst):
#     print(lst[i])
#     i += 1
# print("End of while Loop.")

# # #Updating elements of Lists
# lst = list(range(5))
# print(lst)
# lst.append(9) #=> append the new element to the list.
# print(lst)

# #Updating the value means changing the value of the element in the list. This is done by accessing the specific element
# #indexing or slicing and assigning a new value.
# lst[1] = 8
# print(lst)
# lst[1:3] = 10, 11
# print(lst)

# #Deleting an element from list can be done by using del statement.
# del lst[1]
# print(lst)

# #we can also delete the element using the remove() method. In this method we need to pass the element to be deleted.
# lst.remove(11)
# print(lst)
# # lst.remove(22)
# # print(lst) #ValueError: list.remove(x): x not in list

# #Reversing the order of the list using list.reverse()
# lst1 = [1,3,5,7,9]
# # lst2 = lst1.reverse(lst1) #Error: reverse() does not take any arguments.
# # lst2 = lst1.reverse() #Output = NONE because reverse() method does not support assignment.
# lst1.reverse()
# print(lst1)

# #List concatenation
# x = [10, 20, 30, 40, 50]
# y = [5, 15, 25, 35, 45]
# print(x+y)

# #List repeatation
# x = [10, 20, 30, 40, 50]
# print(x * 2)

# #Membership in Lists
# x = [1, 2, 3, 4, 5,]
# y = 2
# z = 6
# print(y in x)
# print(z in x)
# print(z not in x)
# print(y not in x)

# #Copying of Lists
# a = [1,2,3,4,5]
# b = a
# a[2] = 8
# a.append(6)
# print(a)
# print(b)
# x = [1, 2, 3, 4, 5,]
# y = x.copy()
# x.append(9)
# print(x)
# print(y)

# #List Preceedings
# num = [10, 20, 30, 40, 50]
# n = len(num)

# num.append(60)
# print("Appended list on adding element 60 is: ", num)

# num.insert(2,25)
# print("List after Insertion is:", num)

# num1 = num.copy()
# print("Newly created list num1: ", num1)

# num.extend(num1)
# print("Num after appending num1: ", num1)

# n = num.count(50)
# print(n)

# num.remove(50)
# print('num after removing 50:', num)

# num.pop()
# print('num after removing ending element: ',num)

# num.sort()
# print('num after sorting: ', num)

# num.reverse()
# print('num after reversing: ', num)

# num.clear()
# print('number after removing all the elements: ', num)

# #Min and Max in a List.
# num = [10, 20, 30, 40, 50]
# print(min(num))
# print(max(num))

# #sorting of list elements
# x = [3,1,5,2,9,7,6]
# x.sort()
# print("Ascending order of the list is:", x)
# x.sort(reverse=True)
# print("Descending order of the list is:",x)

#=========================="End of Lists"========================================

# #Tuple
# tup1 = (1,2,3,4,5)
# print(type(tup1))
# print(tup1)

# lst1 = [9,8,7,6,5]
# print(type(lst1))
# tup2 = tuple(lst1)
# print(tup2)
# print(type(tup2))

# #Assigning/Slicing tuple elements:
# print(tup2[0])
# print(tup2[1])
# print(tup2[-1])
# print(tup2[-5: ])
# print(tup2[-5: : 2])

# #Basic operations on Tuples:
# tup1 = (1,2,3,4,5)
# print(len(tup1))        #Gives the length of the tuple.
# tup2 = ((tup1) * 3)     #Repeatation of tuple.
# print(tup2)
# tup3 = tup1 + tup2      #Concatenation of 2 or more tuples.
# print(tup3)
# x = 2
# print(x in tup1)        #Membership/Searching/Iterating if element is available in tuple.

# #Functions on Tuples:
# tup1 = (1,2,3,4,5)
# print(min(tup1))          #Min value of the tuple.
# print(max(tup1))          #Max value of the tuple.
# print(tup1.count(2))      #Prints no.of times element '2' is found in tup1.    
# print(tup1.count(10))     #Prints 0 if the element is not found in the tup1.
#print(tup1.index(5))       #Prints the first index position of the element '5' in the tup1.
tup2 = 3,1,1,3,4,5
# print(tup2.index(1))        #Prints the first index position of the element '5' in the tup1.
# print(tup2.index(6))        #Prints ValueError if not found in tuple.
print(sorted(tup2))         #Sorts the tuple in Ascending order.
print(sorted(tup2,reverse=True))        #Sorts the tuple in Descending order.
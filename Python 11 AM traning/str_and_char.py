# #Understanding string indexing.
# # s1 = "Core Python"
# # print(s1[0])

# #Program to access each element of string in forward and reverse method using while loop.
# s1 = 'Core Python'
# n = len(s1)
# print(n)
# i = 0
# while i < n: #if we write i<=n, then we get indexerror.
#     print(s1[i])
#     i += 1
# print('-------------------------------')
# print()
# #The "string index out of range" error in Python occurs when you try to access a character in a string at 
# # an index position that doesn't exist. In other words, you're trying to grab a character beyond the 
# # string's length or at a negative index that goes past the beginning of the string.

# s1 = 'Core Python'
# n = len(s1)
# print(n)
# i = -1
# while i >= -n:
#     print(s1[i])
#     i -= 1

# #String slicing
# s = 'Core Python'
# print(s[0])
# print(s[0:4])
# print(s[ : : 1])
# print(s[ : : 2])
# print(s[-1])
# print(s[0: ])
# print(s[-10: -1])

# #Repeating the string
# s = '(Core Python) '
# print(s * 2)

# #String concatenation
# s1 = "Core "
# s2 = 'Python'
# s = s1 + s2
# print(s)

# #Program to know whether a substring exists in main string or not.
# s1 = input("Enter the main string: ")
# s2 = input("Enter the sub string: ")
# if s2 in s1:
#     print("Sub string available in Main string.")
# else:
#     print("Sub string not available in Main string")

# #Removing spaces:
# s1 = '   /M Krishna Aditya.   '
# print(s1.rstrip())
# print(s1.lstrip())
# print(s1.strip())

# #counting substring in string
# s1 = "New Delhi"
# n = s1.count('e')
# print(n)

# #Strings are immutable.
# s1 = 'One'
# s2 = 'Two'
# print(s1)
# print(s2)
# print(id(s1)) #1730298549264
# print(id(s2)) #2552379904896

# s2 = s1
# print(s1)
# print(s2)
# print(id(s1)) #2300699513872
# print(id(s2)) #2300699513872

# #string replace
# str = 'This is a beautiful flower.'
# s3 = str.replace('flower', 'rose')
# print(s3)

# text = "Hello world, hello world!"
# new_text = text.replace("world", "Python") 
# print(new_text)

# #Splitting and Joining strings
#SPLITTING
# str = 'one, two, three, four'
# print(type(str)) #<class 'str'>
# str1 = str.split(',')
# print(str1) #['one', ' two', ' three', ' four']
# print(type(str1)) #<class 'list'>

# #Program to accept and display group of numbers.
# num = input("Enter the numbers separated with ,:")
# lst = num.split(',')
# print("List displayed after using split mentod is :", lst)

# #JOINING
# str = ('One', 'Two', 'Three')
# str1 = '-'.join(str)
# print(str1)

# #Changing case of a string
# str = 'Refer to the example shown in str_and_char.py to have clear understanding.'
# str1 = str.upper()
# print(str1)
# str2 = str.lower()
# print(str2)
# str3 = str.swapcase()
# print(str3)
# str4 = str.title()
# print(str4)


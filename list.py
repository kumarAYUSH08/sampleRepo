lst = []
print(lst)
print(type(lst))

"""
Creation
Access elements
Adding elements : append,extend,insert
Removing elements : remove, del, pop
Sorting : .sort, sorted
Reverse : [::-1], .reverse
Slicing
Split
Copies vs Views
Functions : map, filter
Methods
List comprehension
Nested loops and Flattening

"""

# In list, lst.# are all inline operation
# i.e. all operation will be performed here on the same list,tuple etc.
# new list wont be returned

# Creation
# List of integers
a = [1, 2, 3, 4, 5]
# List of strings
b = ['apple', 'banana', 'cherry']
# Mixed data types
c = [1, 'hello', 3.14, True]
# From a tuple :: Using the list() Constructor
a = list((1, 2, 3, 'apple', 4.5))  
print(a)
# Creating a List with Repeated Elements
# Create a list [2, 2, 2, 2, 2]
a = [2] * 5
# Create a list [0, 0, 0, 0, 0, 0, 0]
b = [0] * 7

# Accessing list elements
a = [10, 20, 30, 40, 50]
# Access first element
print(a[0])    
# Access last element
print(a[-1])

lst = [1,2,3,1,2,2,4]
print(len(lst))
print(lst.count(2))


# Adding Elements into List 
# .append(), .extend(), .insert()

# Append : 
lst.append(5)
print(lst)
lst2= [7,8,1,9]
lst.append(lst2)  # appends list as a complete list not as elements
print(lst)
lst.append('five')
print(lst)

# Extend
lst = [1,2,3,1,2,2,4]
lst2= [7,8,1,9]
print("Extend")
lst.extend(lst2)
print(lst)

# Insert
print("Insert")
lst.insert(2,'three')
print(lst)

# Adding/Joining 2 list
a = [1, 2, 3]
b = [4, 5, 6]
# Merge the two lists and assign
# the result to a new list
c = a + b
print(c)


# Delete : Removing element from list
# lst.remove(element)   --> removes element from the list
# del lst[index_num]    --> removes element with its index num from the list
print("Delete")
lst.remove(1)  #removes 1st occurance of 1 from the list and not all
print(lst)
lst.remove(2)  #removes 1st occurance of 2 from the list and not all
print("Second removal")
print(lst)
del lst[1] # removes element at index 1
print("Third removal")
print(lst)
lst.pop(2) # removes element at index 2

if 2 in lst:
    print(True)


# Sorting
print("Sorting")
lst = [1,2,3,1,2,2,4]
sorted_lst = sorted(lst)   # sorts lst and saves the new list in sorted_lst, no change in lst
print(sorted_lst)
print("og list ", lst)
rev = sorted(lst, reverse=True)
print(rev)
print("HEREEE")
a = lst.sort()   # does nothing, returns None
print(a)
lst.sort()  #in-line op
print(lst)


# Reverse  
# Best is In-place(lst.reverse) and list slicing ([::-1])
# (a) in-place operation 
a = [1, 2, 3, 4, 5]
print("Reverse")
# Reverse the list in-place operation
a.reverse()
print(a)

# (b) Using List Slicing
a = [1, 2, 3, 4, 5]
# Create a new list that is a reversed list of 'a' using slicing
rev = a[::-1]
print(rev)
a = [1, 2, 3, 4, 5]
# Use reversed() to create an iterator
# and convert it back to a list
rev = list(reversed(a))
print(rev)

# (c) Using the reversed()
a = [1, 2, 3, 4, 5]
# Use reversed() to create an iterator
# and convert it back to a list
rev = list(reversed(a))
print(rev)

# (d) Using a Loop (creating new reversed list)
a = [1, 2, 3, 4, 5]
# Initialize an empty list to store reversed element
res = []
# Loop through each item and insert
# it at the beginning of new list
for val in a:
    res.insert(0, val)
print(res)




# Slicing
print("List Slicing")
lst = [1, 2, 3, 4]
sliced_lst = lst[:]
sliced_lst[0] = 99
print(lst)         # Output: [1, 2, 3, 4] (unchanged)
print(sliced_lst)  # Output: [99, 2, 3, 4] (new list)



# Split
# Syntax :: list_name[start : end : step]
print("string.split examples")
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get elements from index 1 to 4 (excluded)
print(a[1:4])

s = "ayush is a swe"
lst = s.split(' ')
print(lst)
new = ' '.join(lst)
print(new)

print("Output > items in a string")
for ele in s:
    print(ele)  # default end is \n
for ele in s:
    print(ele, end='')

print()
print("Output > items in a list")
for ele in lst:
    print(ele)  # default end is \n
for ele in lst:
    print(ele, end=' ')
print()

# List comprehension
squares = [i**2 for i in range(10)]
print(squares)

# Views vs. Copies
# Operation	    Behavior	                                Example

# Slicing	    Creates a shallow copy (not a view)	        lst[:2]
# reversed	    View	                                    reversed(lst)
# enumerate	    View-like	                                enumerate(lst)
# map/filter	View-like (iterators)	                    map(func, lst)


"""
# List Functions

Function	Purpose
max()	    Returns the largest element
min()	    Returns the smallest element
sum()	    Returns the sum of elements
len()	    Returns the number of elements
sorted()	Returns a sorted list
all()	    Checks if all elements are truthy
any()	    Checks if at least one element is truthy
reversed()	Iterates through the list in reverse
enumerate()	Index-value pairs
map()	    Applies a function to each element
filter()	Filters elements based on a condition
"""

lst = [10, 20, 5, 30, 15]
print(min(lst))  # Output: 5
lst = [10, 20, 30]
print(sum(lst))  # Output: 60
lst = [10, 20, 30, 40]
print(len(lst))  # Output: 4
lst = [10, 20, 5, 30]
print(sorted(lst))         # Output: [5, 10, 20, 30]
print(sorted(lst, reverse=True))  # Output: [30, 20, 10, 5]
lst = [1, 2, 3]
print(all(lst))  # Output: True
lst = [0, 1, 2]
print(all(lst))  # Output: False
lst = [0, 0, 1]
print(any(lst))  # Output: True
lst = [0, 0, 0]
print(any(lst))  # Output: False
lst = [10, 20, 30]
print(list(reversed(lst)))  # Output: [30, 20, 10]
lst = ['a', 'b', 'c']
for idx, val in enumerate(lst):
    print(idx, val)
# Output:
# 0 a
# 1 b
# 2 c

lst = [1, 2, 3, 4, 5]
# Filter : Syntax : filter(function, iterable) : returns filter object
even = filter(lambda x: x % 2 == 0, lst)
print(list(even))  # Output: [2, 4]
fruits = ['apple', 'banana', 'cherry']
res = map(str.upper, fruits)   # applies on all elements
print(list(res))


# List Methods
# Let’s look at different list methods in Python:

# append(): Adds an element to the end of the list.
# copy(): Returns a shallow copy of the list.
# clear(): Removes all elements from the list.
# count(): Returns the number of times a specified element appears in the list.
# extend(): Adds elements from another list to the end of the current list.
# index(): Returns the index of the first occurrence of a specified element.
# insert(): Inserts an element at a specified position.
# pop(): Removes and returns the element at the specified position (or the last element if no index is specified).
# remove(): Removes the first occurrence of a specified element.
# reverse(): Reverses the order of the elements in the list.
# sort(): Sorts the list in ascending order (by default).

# List Comprehension
# Syntax :  [expression for item in iterable if condition]
a = [2,3,4,5]
res = [val ** 2 for val in a if val%2==0]
print(res)

# Nested Loops
# Creates a list of tuples representing all combinations of (x, y)
# where both x and y range from 0 to 2.
coordinates = [(x, y) for x in range(3) for y in range(3)]
print(coordinates)

# Flattening a list of lists
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = [val for row in mat for val in row]
print(res)
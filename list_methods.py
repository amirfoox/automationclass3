import random

# print all the methods:
# print(dir([]))

# list all the "non-magic" methods (no __method__)
print(list(filter(lambda x: not x.startswith("__"), dir([]))))


# append, add an element to a list
a = [1, 2, 3]
a.append(11) # this is how you append
print(a)
a = a.append(11)  # this is NOT how you append!
print(f" after assign an append: a= a{a}")

a = "I LIKE cars!"
a.capitalize() # this is NOT how to do string operations!
print(a)
a = a.capitalize()  # this is how you do string operations
print(a)


a = [1, 2, 3]
b = a
print(f"b is a is {b is a}, so changing b will also change a, and vice versa")
b[0] = 99
print(a, b)

# to copy the list instead of mirror it:

a = [1, 2, 3]
b = a.copy()
print(f"b is no longer a now")
b[0] = 99
print(a, b)

# clears the list:
a.clear()
print(a)

# count the number of 2 in a list
a = [1, 2, 3, 2, 3, 4, 2, 5, 2]
print(f"2 shows up {a.count(2)} times")

# extend same as +
a = [1, 2, 3]
b = [9, 10, 11]
a.extend(b)
print(a, a+b)
print (a.index(10)) # return index
a.insert(2, 99)
print(a)
print(a.pop(), a.pop(2))
print(a)  # pop takes variables from the list, now they are gone
a.remove(9)
print(f"a after removing the value 9: {a})")

a.reverse()   # actually reverses the list, it's now reversed
print(a)
print(a[::-1]) # does the same thing as reverse, but it only prints - it doesn't actually change the list


# how to sort a list:
a = []
for i in range(100):
    a.append(random.randint(1, 100))
print(f"unsorted A; {a}")
a.sort()
print(f"sorted A; {a}")

# reverse the sort:
a.sort(reverse=True)
print(f"reverse sorted a: {a}")



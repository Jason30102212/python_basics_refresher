# 10.ListFunctions

numbers = [4, 8, 15, 16, 23, 42]
strings = ["One", "Two", "Three", "Four", ]

#strings.extend(numbers) # Append to end of list

strings.extend("Five") # Append each character as a value to list
strings.append("Five") # Append as string to list
strings.insert(2, "Two and a half") # First arg is indedx of list, second is value
strings.remove("Three") # Remove a specific string

print(strings)

strings.clear() # Clears a list

print(strings)

strings = ["One", "Two", "Three", "Four", ]
strings.index("Three") # Index of specified value
# strings.index("QQQ") # ERROR

strings = ["One", "Two", "Three", "Four", "Four", "Four" ]
print(strings.count("Four")) # Counts number of appearances

print(strings.sort()) # Sort in desending order
print(strings.reverse())

#stringsTwo = strings #This sets a reference to strings and 
#print(strings)
#stringsTwo.clear()
#print(strings)

stringsTwo = strings.copy() # Creats a new list, not a reference


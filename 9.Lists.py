# 9.Lists

listOne = ["One", "Two", "Three", "Four", "Five"]

listTwo = ["One", 2, True]
 
print(listOne) # Print entire list
print(listOne[1]) # Print by index
print(listOne[-1]) # Print from last
print(listOne[1:]) # Element at position one and all elements after
print(listOne[:-1])

listOne[1] = "ZZZ" 
print(listOne[1])
print(listOne)
# 19.ForLoop

array = ["one", "two", "three"]

for letter in "This is a string":
    print(letter)
    
for name in array:
    print(name)

for index in range(3, 10):
    print(index)
    
for index in range(len(array)):
    print(index)

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not First")
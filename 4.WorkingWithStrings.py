# 4.WorkingWithStrings

print("Test String") # Basic string
print("Test\nString") # New line (\n)
print("Test \"String") # Escape character (\")

# concat
phrase = "This is "
print(phrase + "a test string")

# string functions
phrase = "Random Phrase"
print(phrase.upper()) # Conver to upper
print(phrase.isupper()) # determines if upper
print(phrase.upper().isupper()) #conver to upper and determine if so
print(len(phrase)) # Length of string
print(phrase[0]) # Print specific letter at location
print(phrase.index("a")) # Print index of first instance
# print(phrase.index("z")) # Print index of first instance #Error. No instance of 'Z'
print(phrase.replace("Phrase", "String"))

# custom function
randomString = "This is a random string"

def stringFormatter(stringToFormat):
    formattedString = stringToFormat.upper()
    return formattedString

print(stringFormatter(randomString))
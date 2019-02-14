# 22.BuildATranslator

# All vowels become g


def changeVowels(string):
    
    translation = ""
    
    for letter in string:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation



print(changeVowels(input("Enter a string: ")))





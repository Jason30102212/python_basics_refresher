# 24.TryExcept

#try:
#    number = int(input("Enter a number: "))
#    print(number)
#except:
#    print("Must enter an Int")

#try:
#    #value = 10 / 0
#    number = int(input("Enter a number: "))
#    print(number)
#except ZeroDivisionError:
#    print("Divided by zero")    
#except ValueError:
#    print("Invalid Input")

try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)    
except ValueError:
    print("Invalid Input")
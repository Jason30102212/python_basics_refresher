# 15.BuildingABetterCalculator

firstNum = input("Please enter a number: ")
secondNum = input("Please enter a second number: ")
operator = input("Please enter an operator: ")

if operator != "+" and operator != "-":
    operator = input("Please enter an operator")

def calculator(firstNum, secondNum, operator):
    if operator == "+":
        return float(firstNum) + float(secondNum)
    elif operator == "-":
        return float(firstNum) - float(secondNum)
    else:
        return "ERROR";
    
calculator(firstNum, secondNum, operator)
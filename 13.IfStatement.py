#13.IfStatement
b = 3

if b == 2:
    print(str(b) + " = 2")
else:
    print(str(b) + " != 2")
    

def ifFunction(string):
    if string == "go":
        print("GO!")
    else:
        print("STOP!")

ifFunction("go")

def ifTrueFunction(male, tall):
    if male and tall:
        print("Both Male and Tall")
    elif male or tall:
        print("Male or Tall")
    else:
        print("Either Female and/ or Short")

maleVar = False
tallVar = False

ifTrueFunction(maleVar, tallVar)
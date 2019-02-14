# 25.ReadingFiles

# Open file
# open("employees.txt", "r")

# r=read
# w=write
# a=append
# r+=read and write

# Open File
employee_file = open("employees.txt", "r")

# Make sure file is readable
print(employee_file.readable())

## Print File
#print(employee_file.read())
#
## Print Line of File
#print(employee_file.readline()) # Read first line. Move cursor
#print(employee_file.readline()) # Read second line.

for employee in employee_file.readlines():
    print(employee)
    

#print(employee_file.readlines()[2])

# Close File
employee_file.close()

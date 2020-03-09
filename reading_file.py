employee_file = open("employee.txt", "r")

print(employee_file.readable())

# displaying entire content of file in one go
#print(employee_file.read())

#reading and displaying content of file line by line
#print(employee_file.readline())
#print(employee_file.readline())

# Take all of the lines inside of our file and put them inside of an array ( by array we mean list)
#print(employee_file.readlines())

# To access a specific line we can refer to its index value
#print(employee_file.readlines()[1])

#We can make use of For loops
for employee in employee_file.readlines():
    print(employee)

#closing file
employee_file.close()
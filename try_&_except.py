try:
    #value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
#displaying error as variables (err)
except ZeroDivisionError as err:
    print("Divided by zero")
    print(err)
except ValueError:
    print("Inavlid Input")
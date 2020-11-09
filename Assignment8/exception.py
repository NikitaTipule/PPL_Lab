#EXception handling 

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))


try: 
    print("resourse opened")
    print(a/b)
    k = int(input("Enter a number : "))


except ZeroDivisionError as e:
    print("Hey, you are dividing a number by zero :  ", e)

except ValueError as e:
    print("Invalid input ")

except Exception as e:
    print("Something went wrong : ",e)

finally:
    print("resourse closed")



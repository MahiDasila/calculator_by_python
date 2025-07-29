print(" CALCULATOR")
var1 = float(input("Enter a number: "))
var2 = float(input("Enter another number: "))

print("Enter your choice: add, subtract, multiply, divide, modulus, exponentiation,floor division")
choice = input("Choice: ")
if choice == "add":
    print(var1 + var2)
elif choice == "subtract":
    print(var1 - var2)
elif choice == "multiply":
    print(var1 * var2)
elif choice == "divide":
    if var2 != 0:
        print(var1 / var2)
    else:
        print("Error: Denominator must not be zero.")
elif choice == "modulus":
    print(var1 % var2)
elif choice == "exponentiation":
    print(var1 ** var2)
elif choice =="floor division":
    print(var1//var2)    
else:
    print("Invalid choice.")
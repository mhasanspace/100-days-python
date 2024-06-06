# Input block

# num1 = float(input("Enter First Number:"))

# operator = input("What You Want:")

# num2 = float(input("Enter Second Number:"))


# claculation block

# add = (num1 + num2)
# minus = (num1 - num2)
# mutiply = (num1 * num2)
# division = (num1/num2)


# condition block

# if operator == "+":
#     print(f"Result: {add}")
# elif operator == "-":
#     print(f"Result: {minus}")
# elif operator == "*":
#     print(f"Result: {mutiply}")
# elif operator == "/":
#     print(f"Result: {division}")
# else:
#     print("Not a valid operator")


# Advance calculator

while True:
    try:
        num1 =float(input("Enter Number:"))
        operator = input("What You Want (+, -, *, /):")
        num2 = float(input("Enter Number:"))
    except ValueError:
        print("Invalid Input: Please enter number's only.")
        continue

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            result = "Error: division by zero"
        else:
            result = num1 / num2
    else:
        result = "Invalid Operator"
    
    finalResult = f"Result: {result}"

    print (finalResult)

    choice = input("To continue type [y] or to exit type [n]:").lower()

    if choice == "n":
        break
    elif choice not in ("[y] or [n]"):
        print("Invalid Choice. Please enter 'y' or 'n'")
    print("Thank you for using the calculator!")



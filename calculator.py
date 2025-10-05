print("Hi guest this is calculator there u can calculating anything what u want enjoy!")

while True:
    tutorial = input("Do u want tutorial?(Yes/No) ")
    if tutorial == "Yes" or tutorial == "yes":
        print("Ok here is: \nFirst you write me the first number, then you write the second number, and finally you must write the action you want to perform with these numbers.")
        break
    elif tutorial == "No" or tutorial == "no":
        print("OK, here's a calculator")
        break
    else:
        print("I think u wrote the wrong thing, try again.")

first_number = float(input("Write ur first number: "))
second_number = float(input("Write ur second number: "))
action = input("Write ur action: ")

if action == "+":
    print("Result:", first_number + second_number)
elif action == "-":
    print("Result:", first_number - second_number)
elif action == "*":
    print("Result:", first_number * second_number)
elif action == "/":
    if second_number != 0:
        print("Result:", first_number / second_number)
    else:
        print("Error: division by zero!")
else:
    print("Unknown action! Try one of: +, -, *, /")
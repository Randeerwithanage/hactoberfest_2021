# <<<<<<<<<<<<<<..........make a simple calculator for beginers for the payton ..........>>>>>>>


def add(x, y):          # <--------adds two numbers
    return x + y


def subtract(x, y):     # <---------subtracts two numbers
    return x - y


def multiply(x, y):     # <-------- multiplies two numbers
    return x * y


def divide(x, y):       # <-------- multiplies two numbers
    return x / y

def rem(x,y):
    return x%y

# print to user.....

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Remainder")

while True:
   
   
    choice = input("Enter choice(1/2/3/4/5): ")        # <----------take input from the user

    
    if choice in ('1', '2', '3', '4','5'):               #<---------- check if choice is one of the four options
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            
        elif choice == '5':
            print(num1, "%", num2, "=", rem(num1, num2))
        
        # check if user wants another calculation



        # break the while loop if answer is no


        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":

          break
    
    else:
        print("Invalid Input")     #<_______----print invalid to user

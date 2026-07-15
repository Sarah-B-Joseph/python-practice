print("Options: + - * / ")
print("Type 'exit' to quit")
op = input("Enter your option: ")
print()

while True:
    if op == "exit":
        break

    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))

    if op not in "+-*/":
        print("Enter a valid option")
    elif op =="+":
        print(n1 + n2)
    elif op == "-":
        print(n1 - n2)
    elif op == "*":
        print(n1 * n2)
    elif op == "/":
        if n2 != 0:
            print(n1/n2)
        else:
            print("Divide by Zero Error")
    print()
    print("To continue enter an option")
    print("If you wish to discontinue, type 'exit'")
    op = input("Enter your option: ") 
    

       
    
    
    

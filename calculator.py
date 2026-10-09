#function for addition
def addition(a,b):
    return (a+b)

#function for subtraction
def subtraction(a,b):
    return (a-b)

#function for miltiplication
def multiplication(a,b):
    return a*b

#function for division
def division(a,b):
    try:
        return a/b
    #catch an exceptions
    except ZeroDivisionError:
        print("Cannot be divided by zero")

#main function
def main():
    while(1):
        #take inputs from user
        a,b = map(int, input(print("Enter two numbers:")).split())
        #menu for operations
        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
        choice = int(input(print("Choose any operation number:")))
        if choice==1:
            print(addition(a,b))
            
        elif choice==2:
            print(subtraction(a,b))
            
        elif choice==3:
            print(multiplication(a,b))
            
        elif choice==4:
            print(division(a,b))
            
        elif choice>4:
            print("Invalid choice")
        if input(print("Do you want to continue? (y/n)")) == 'n':
            break

#calling main function        
if __name__ == "__main__":
    main()       


    
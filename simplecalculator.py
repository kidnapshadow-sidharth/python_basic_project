# this is a simple calculator made with sidharth
# using with python 
print("Welcome to calculator 1.1 made with love")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print('''Select your choice: 
                        Press 1. for Adding
                        Press 2. for substract
                        Press 3. for multiply
                        Press 4. for divide
                        Press 0. for exit''')

choice = int(input("Enter your choice :  "))

if choice == 0:
    exit()
elif choice == 1:
    result= num1+num2
    print("the addition of these two number is ",result)
elif choice == 2:
    result= num1-num2
    print("the substraction of these two number is ",result)
elif choice == 3:
    result= num1*num2
    print("the multiplication of these two number is ",result)
elif choice == 4:
    result= num1/num2
    print("the division of these two number is ",result)
else:
    print("wrong input")
    
        


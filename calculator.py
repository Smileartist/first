print(" SELECT ANY MATHEMATICAL OPERATOR FROM :- (+ , - , * , /)")

first = input("enter your first number = ") 
second = input("enter your second number = ")
first=int(first)
second=int(second)

operator = input("enter your operator here :- ")
if operator == "+" :
    print(first + second)
    
elif operator == "-"  :
     print(first - second)

elif operator == "*"  :
     print(first * second)     

elif operator == "/"  :
     print(first / second) 

else :
    print("invalid operation")      

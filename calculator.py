from art import callogo
print(callogo)
def add(x, y):
    return x+y
def sub(x, y):
    return x-y
def mul(x, y):
    return x*y
def div(x, y):
    if y!=0:
        return x/y
    else:
        return "Cannot divide by zero"
operations = {'+':add, '-':sub, '*':mul,'/':div}

while 1:
    operator = input("Enter an operator (+, -, *, /) or 'stop' to exit: ").lower() 
    
    if operator== 'stop':
        print("Calculator stopped.")
        break
    if operator not in operations:
        print("Invalid operator.")
        continue
    
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    total=operations[operator](num1, num2)
    print("Result:", total)
    callogo="""
 _____________________
|  _________________  |
| |              /  | |
| |       /\    /   | |
| |  /\  /  \  /    | |
| | /  \/    \/     | |
| |/  SHREYA'S CAL  | |
| |_| |
|  __ __ __ __ __ __  |
| ||||||| |
| ||||||| |
| ||||||| |
| ||||||| |
| ||||||| |
| ||||||| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |||| || |
| | 4 | 5 | 6 | | - | |
| |||| || |
| | 1 | 2 | 3 | | x | |
| |||| || |
| | . | 0 | = | | / | |
| |||| || |
|_|
"""

logo = """
    __  ___       __             
   / / / ()__ / /  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
// ////\, // //\//     
   / /  //_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / // // / |/ |/ /  __/ /    
//\/|/|/\/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|/()
""" 
'''def title_name():
    f_name = input("Enter Your first name: ").lower()
    l_name = input("Enter you last name: ").lower()
    t_name = (f_name +' '+l_name).title()
    print(t_name)
title_name()  '''
 
# Simple Calculator 

def add(n1,n2):
    print(f"{n1}+{n2}={n1+n2}")
    return n1+n2
def sub(n1,n2):
    print(f"{n1}-{n2}={n1-n2}")
    return n1-n2
def mul(n1,n2):
    print(f"{n1}*{n2}={n1*n2}")
    return n1*n2
def div(n1,n2):
    print(f"{n1}/{n2}={n1/n2}")
    return n1/n2
n1=float(input("Enter the first number: "))
print("""
+
-
*
/
""")
operator=['+','-','*','/']
_continue = 'y'
while _continue =='y':
    operation=input("Pick an operation: ")
    n2=float(input("Enter the second number: "))

    if operation==operator[0]:
        n1=add(n1,n2)
        
    elif operation==operator[1]:
        n1=sub(n1,n2)
        
    elif operation==operator[2]:    
        n1=mul(n1,n2)
        
    elif operation==operator[3]:
        n1=div(n1,n2)
        
    else:
        print("Invalid operation")
    _continue=input("Type 'y' if you would like to continue or type 'n' to start new calculation: ")





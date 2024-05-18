#function to check if a number is even or odd
def check_number():
    a=int(input('enter number'))
    if a%2==0:
        print(f'{a} is even')
    else:
        print(f'{a} is odd')
##call the function
check_number()
##write a function to calculate area of a triangle
def calc_area():
    b=float(input('enter base'))
    h=float(input('enter height'))
    print(0.5*b*h)
calc_area()

##parameters and arguments
def check_number(num):
    if num%2==0:
        print('even')
    else:
        print('odd')
check_number(20)

##function to calculate area using parameters and take users input
def tr_area(x,y):
    area=x*y*0.5
    print(area)

base=int(input('enter base'))
height=int(input('enter height'))
tr_area(base,height)

##return....
def tr_area(x,y):
    area=x*y*0.5
    return area

base=int(input('enter base'))
height=int(input('enter height'))
tr_area(base,height)
##if you want to display in terminal
term=tr_area(base,height)
print(term)

##funtion to calculate gross salary
def gross(s,b):
    gross_salary=s+b
    return gross_salary

basic=float(input('enter basic salary'))
benefits=float(input('enter benefits'))
    
gross(basic,benefits)

terminal=gross(basic,benefits)
print(terminal)

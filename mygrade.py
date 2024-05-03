marks=int(input('enter marks'))

if (marks>=0 and marks<=100):
    if (marks>=70):
        print('A')
    elif (marks>=60):
         print('B')
    elif (marks>=50):
         print('C')
    elif (marks>=40):
         print('D')
    else:
         print('E')



else:
        print('invlid marks')


##Take three inputs from a user, separately. Print the largest of the number
num1=input('enter Num1')
num2=input('enter Num2')
num3=input('enter Num3')

if (num1>num2 and num1>num3):
     print(num1)
     print(type(num1))
elif(num2>num1 and num2>num3):
     print(num2)
     print(type(num2))
else:
     print(num3)
     print(type(num3))


##Take as input from a user the temperature if the temperature is above 30°C display
## “The temperature is too high”, otherwise display “Normal temperature”
temp=int(input('enter temp'))
if (temp>=0 and temp<=100):
     if (temp>30):
          print('Too high')
     else:
          print('normal Temp')
else:
     print('Invalid Temp')
    


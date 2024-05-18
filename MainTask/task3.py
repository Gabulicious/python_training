##Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking
##if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
num=input('enter number')
if num.startswith('+254') and len(num)==13:

    print(num)
elif num.startswith('07') and len(num)==10:
    
    print('+254'+num[1:])
elif num.startswith('01') and len(num)==10:
    
    print('+254'+num[1:])
elif num.startswith('1') and len(num)==9:
    
    print('+254' +num)
elif num.startswith('7') and len(num)==9:

    print('+254' +num)
elif num.startswith('254') and len(num)==12:
    print('+' + num)
else:
    print('invalid')


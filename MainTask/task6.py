##Write a program input a password. Give them only 4 attempts to check the passwords entered against “admin@123”.
##If the password is correct access is granted. After you show them a message , the account is blocked.

# total=4
# correct='admin@123'
for i in range(0,4):
 password=input('enter password')
 if i==3:
  print('blocked')
 if password=='admin@gmail.com':
        print('correct')
 else:
      print('wrong')
      
           
 
 
 
        

##Write a program that takes the email and password as input from a user and checks if they are equal to
##“admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print
##“Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.
for i in range(0,4):
 password=input('enter password')
 email=input('enter email')
 if i==3:
  print('blocked')
 if password=='Admin@123' and email=='admin@mail.com':
        print('login successful')
        if password!='Admin@123':
            print('wrong password')
        if email!='admin@mail.com':
            print('wrong email')
 else:
      print('wrong')
else:
    print('blocked')
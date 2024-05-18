##Write a program that displays a numbers 1 to 50 inside a list.
lst =list(range(1,51))
print(lst)

##From 1 above display the ones divisible by 7 or 5 inside a list.
List=[]
for i in lst:
# if (lst>=1 and lst<=50):
    if (i%7==0 or i%5==0):
        List.append(i)
    # else:
        # print('')
# else:
    # print('error')
print(List)

##Find sum and average of values in the range between 10 to 40.
lst3=[]
total=0
for i in range(10,41):
    total+=i
    lst3.append(i)
    avg=total/len(lst3)

print(total)
print(avg)


##Put in a list the first 10 odd numbers between 10 to 50. 
list2=list(range(10,51))
# print(list2)

lis=[]
for i in list2:
    if (i%2!=0):
        lis.append(i)
        if len(lis)==10:
            break

print(lis)

##write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
num=int(input('enter number'))

for i in range(1,11):
    x=i*num
    print(f'{i}*{num}={x}')

##write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
lst5=[]
even=list(range(1,51))
for i in even:
    if (i%2==0):
        lst5.append(i)
       
print(len(lst5))
 

## Display the total quantity of the 3 below.
ls1 = [ ('Jay', 20), ('Mo', 30), ('Mya', 32) ]
total=0
for i in ls1:
    quantity=i[1]
    total+=quantity

print(total)










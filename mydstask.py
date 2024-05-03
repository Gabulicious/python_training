my_ds = [23, 'Jane', (560), ['Lesson', 'Maths', {'currency': 'KES'}], 987, (76,'John')]
##print KES
print(my_ds[3][2]['currency'])
##print 560
print(my_ds[2])
##print Maths
print(my_ds[3][1])
##In the dictionary with the key currency, add another key “amount” with value 90
my_ds[3][2]['amount']=90
print(my_ds)
##Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.


##Change the name “John” to “Jane” . 
index_to_change = my_ds.index((76, "John"))

# Create a new tuple with the updated name
new_tuple = (my_ds[index_to_change][0], "Jane")

# Replace the old tuple with the new one
my_ds[index_to_change] = new_tuple

print(my_ds)



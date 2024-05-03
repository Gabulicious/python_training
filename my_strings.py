first_name='  JoHn  '
last_name=' DoE'
full_name=first_name+" "+ last_name
print(full_name)
first_name=first_name.strip().title()
last_name=last_name.title().strip()
full_name=first_name+' '+ last_name

print(full_name)
print(len(first_name))

#check its an email
email='john@gmail.com'
print(email.count('@')==1)
#split-breaks a string
st='this is my bag'
print(type(st.split(' ')))

#every variable belongs to certain class


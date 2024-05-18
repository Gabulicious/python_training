##Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days 

my=0
mm=0
md=0
today=str(datetime.datetime.today()).split(' ')[0].split('-')
ty=int(today[0])
tm=int(today[1])
td=int(today[2])
while 1== 1:
    dob = input('enter DOB (dd-mm-yyyy):')
    dmy = dob.split('-')
    if len(dmy)==3:
        d=int(dmy[0])
        m=int(dmy[1])
        y=int(dmy[2])
        if(y<2025) and (m<13) and (d<32):
            if not (m==2 and d>29):
                my=ty-y
                mm=tm-m
                md=td-d
                print(f'You are{my} years,[mm]months and {md} days old')

def calc_gross(s,b):
    gross_salary=s+b
    return gross_salary

basic=float(input('enter basic salary'))
benefits=float(input('enter benefits'))
    
calc_gross(basic,benefits)

gross=calc_gross(basic,benefits)
print(gross)

##function to calc NHIF
def calc_Nhif(gross):
       
 nhif=0
 if (gross>=0 and gross<=5999):
        nhif=150
    
 elif(gross>=6000 and gross<=7999):
        nhif=300
    
 elif (gross >= 8000 and gross <= 11999):
        nhif= 400
    
 elif (gross >= 12000 and gross <= 14999): 
        nhif= 500
    
 elif (gross >= 15000 and gross <= 19999): 
    nhif= 600
    
 elif (gross >= 20000 and gross <= 24999):
        nhif= 750

 elif (gross >= 25000 and gross <= 29999):
        nhif= 850
    
 elif (gross >= 30000 and gross <= 34999):
        nhif= 900
    
 elif (gross >= 35000 and gross <= 39999):
        nhif= 950
    
 elif (gross >= 40000 and gross <= 44999):
        nhif= 1000
    
 elif (gross >= 45000 and gross <= 49999):
        nhif= 1100
    
 elif (gross >= 50000 and gross <= 59999):
            nhif= 1200
    
 elif (gross >= 60000 and gross <= 69999):
            nhif= 1300
    
 elif (gross >= 70000 and gross <= 79999):
        nhif= 1400
    
 elif (gross >= 80000 and gross <= 89999):
        nhif= 1500

 elif (gross >= 90000 and gross <= 99999): 
        nhif= 1600
 else:
       nhif=1700

 return nhif

## finding nssf
def calc_nssf(gross,rate=0.06):
       if gross<=18000:
              nssf=gross*rate
       else:
              nssf=18000*rate
              return nssf
       
##calculating nhdf
def calc_nhdf(gross,rate=0.015):
       nhdf=gross*rate
       return nhdf

##calculating taxable income
def calc_taxable_income(gross,nssf,nhdf):
       taxable_income=gross-(nssf+nhdf)
       return taxable_income

##calculating PAYEE
def calc_payee(taxable_income):
       if taxable_income>=0 and taxable_income<=24000:
              payee=(taxable_income*0.1)-2400
       elif taxable_income>24000:
              payee=(taxable_income*0.25)-2400
       elif taxable_income>32333:
              payee=(taxable_income*0.3)-2400
       elif taxable_income>500000:
              payee=(taxable_income*0.325)-2400
       elif taxable_income>800000:
              payee=(taxable_income*0.35)-2400
              return payee
       
##calculating net_salary
def calc_net_salary(gross,nhif,nhdf,nssf,payee):
       net_salary=gross(nhif+nhdf+nssf+payee)
       return net_salary


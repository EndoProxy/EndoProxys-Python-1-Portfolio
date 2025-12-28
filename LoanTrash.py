#Loan Determination Program


MIN_SALARY = 30000.0 #annual salary
MIN_YEARS = 2 #Years Employed



salary = float(input('Enter your yearly salary: '))

years_employed =  int(input('Enter how many years you have been employed: '))





if salary >= MIN_SALARY:
    if years_employed >= MIN_YEARS:
       print('You qualify for a loan!')
    else:
        print('You do not qualify due to not have the {MIN_YEARS} years required.')


else:
    print('I am sorry but you do not qualify for a loan')

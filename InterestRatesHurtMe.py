print('---Compounding Interest Rate Software---\n\n')

PV = float(input('Please enter your starting principal: '))

R = float(input('Please enter your annual rate: ')) / 100

M = float(input('Now please the approximate number of times per year is your interest annually compounded? '))

T = float(input('How many approximate years with the account be earning interest? '))

FV = PV * (1.0 + R/M)**(M*T)

result = print(f'At the end of {T:.0f} years, you will have: $ {FV:2,.2f}')

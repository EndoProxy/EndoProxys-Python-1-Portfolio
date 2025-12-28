print("---GENERIC TEMPERATURE CONVERTER---:\n\n")
TEMPERATURE = float(input("User, please enter a temperature: "))

FvC = input('Is the temperature that you provided in Fahrenheit or Celsius? \n\nIf Fahrenheit, enter F. If Celsius, enter C: ')
if not (FvC=='F' or FvC=='f' or FvC=='C' or FvC=='c'):
    print('You must enter a valid input. \nPlease enter an F or C')

if FvC == 'F' or 'f':
    if TEMPERATURE > 212:
        print('Temperature can not exceed a value > 212')
    else:
         C_temp = (5.0/9) * (TEMPERATURE - 32)
         print(f'The Celsius equivalent is: {C_temp:.1f}')

if FvC == 'C' or 'c':
    if TEMPERATURE > 100:
        print('Temperature can not exceed a value > 100')
    else:
         F_temp = ((9.0/5.0)* TEMPERATURE) + 32
         print(f'The Fahrenheit equivalent is {F_temp:.1f}')

print('Thank you for using this program')
    

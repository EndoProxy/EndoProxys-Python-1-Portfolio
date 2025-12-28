BASE_HOURS = 40
OVERTIME = 1.5



hours = float(input('Enter the number of hours '))
pay_rate = float(input('Enter the hourly rate '))



if hours > BASE_HOURS:
    OVERTIME_hours = hours - BASE_HOURS

    overtime_pay = OVERTIME_hours * pay_rate * OVERTIME

    total_pay = BASE_HOURS * pay_rate + overtime_pay

else:
    total_pay = hours * pay_rate




print(f'the total pay is ${total_pay:,.2f3}.')




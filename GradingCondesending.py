A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60


score = int(input('What is the test score you got? '))


if score >= A_SCORE:
    print('Your graded score is an A! Absolutely impressive performance.')
elif score >= B_SCORE:
    print('Your graded score is a B! Better, but I know you can strive to do more.')
elif score >= B_SCORE:
    print('Your graded score is a C! Painfully average. Is that what you want to be remembered by?')
elif score >= B_SCORE:
    print('Your graded score is a D! You could have only done worse by failing')
else:
    print('Mother always said you cant teach stupid')

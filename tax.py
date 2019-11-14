# Obtain the user's income
income = float(input('Enter your income in 2018: '))
# Compute tax due
if income > 500000.00:
    tax = 150689.5 + 0.37*(income  - 500000)
elif income > 200000.00:
    tax = 45689.5 + 0.35*(income  - 200000)
elif income > 157500:
    tax = 32089.5 + 0.32*(income  - 157500)
elif income > 82500:
    tax = 14089.5 + 0.24*(income  - 82500)
elif income > 38700:
    tax = 4453.5 + 0.22*(income  - 38700) 
elif income > 9525:
    tax = 952.5 + 0.12*(income  - 9525) 
else: 
    tax = 0.1*(income) 
# Print tax due
print('You owe $',round(tax),' in federal income tax')
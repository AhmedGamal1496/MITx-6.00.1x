originalBalance = 4773
remainingBalance = 4773
annualInterestRate = 0.2
minimumFixedMonthlyPayment = 10

i = 0

while True:
    i = 0
    while i < 12:
        balance = remainingBalance
        monthlyInterestRate = annualInterestRate / 12
        unpaidBalance = balance - minimumFixedMonthlyPayment
        interest = unpaidBalance * monthlyInterestRate
        remainingBalance = round((unpaidBalance + interest),2)
        
        i += 1
    
    if remainingBalance < 0:
        break
    else:
        minimumFixedMonthlyPayment = minimumFixedMonthlyPayment + 10
        remainingBalance = originalBalance

    
print('Lowest Payment: ' + str(minimumFixedMonthlyPayment))
originalBalance = 320000
remainingBalance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0
lowerBound = originalBalance / 12.0
upperBound = (originalBalance * (1 + monthlyInterestRate)**12) / 12.0

while abs(remainingBalance) > 0.01:
    minimumFixedMonthlyPayment = (lowerBound + upperBound) / 2
    balance = originalBalance
    for i in range(12):
        unpaidBalance = balance - minimumFixedMonthlyPayment
        interest = unpaidBalance * monthlyInterestRate
        remainingBalance = round((unpaidBalance + interest),2)
        balance = remainingBalance
    
    if remainingBalance > 0.01:
        lowerBound = minimumFixedMonthlyPayment
    elif remainingBalance < -0.01:
        upperBound = minimumFixedMonthlyPayment
    else:
        break
    
print('Lowest Payment: ' + str(round(minimumFixedMonthlyPayment,2)))
            

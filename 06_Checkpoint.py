# 06 Prepare: Checkpoint
# Jaelee

# user input
print('Please rate the following from 1-10:')
loanSize = int(input('How large is the loan? '))
credit = int(input('How good is your credit history? '))
income = int(input('How high is your income? '))
payment = int(input('How large is your down payment? '))

# check if they should get loan
loan = False
if loanSize >= 5:
    if credit >= 7 and income >= 7:
        loan = True
    elif credit >= 7 or income >= 7:
        if payment >= 5:
            loan = True
        else:
            loan = False

    else:
        loan = False
elif credit < 4:
    loan = False
elif income >= 7 or payment >= 7:
    loan = True
elif income >= 4 and payment >= 4:
    loan = True
else: 
    loan = False

# print whether they get a loan
print()
if loan == True:
    print('You will get a loan!')
else:
    print('You are not eligible for a loan.')

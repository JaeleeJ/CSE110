# 10 Teach: Team Activity
# Jaelee Hutchinson

print('Enter the names and balances of bank accounts (type: quit when done)')

# create lists of accounts and balances
accounts = []
balances = []

# user input
account = ''
while account != 'quit':
    account = str(input('What is the name of this account? '))
    
    if account != 'quit':
        balance = float(input('What is the balance? '))
        balances.append(balance)
        accounts.append(account)

# print account information
if account == 'quit':
    print()
    print('Account Information:')
    total = 0

    for x in range(len(accounts)):
        print(f'{accounts[x]} - ${balances[x]}')
    
    for x in balances:
        total += x
    
    # comput average of balances
    avg = total / len(balances)
    print()
    print(f'Total: ${total}')
    print(f'Average: ${avg}')
    


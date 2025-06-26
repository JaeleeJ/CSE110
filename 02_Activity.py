# 02 Teach: Programming Activity
# Jaelee Hutchinson

print('Please enter the following information:')
print()

#list of inputs
firstName = input('First name: ')
lastName = input('Last name: ')
email = input('Email address: ')
phone = input('Phone number: ')
job = input('Job title: ')
iD = input('ID number: ')

#display
print()
print('The ID Card is:')
print()
print('---------------------------------')
print(lastName.upper() + ',', firstName.capitalize())
print(job.title())
print('ID:', iD)
print()
print(email.lower())
print(phone)
print('---------------------------------')
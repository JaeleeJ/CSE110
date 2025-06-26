# 13 Prepare: Checkpoint
# Jaelee Hutchinson

# function to receive a string and print normally
def display_regular(message):
    print(message)

# function to convert string to upper case
def display_uppercase(message):
    print(message.upper())

# function to convert string to lower case
def display_lowercase(message):
    print(message.lower())

message = str(input('What is your message? '))

# call functions
display_regular(message)
display_uppercase(message)
display_lowercase(message)
# 09 Prepare: Checkpoint
# Jaelee 

# user input
friends = []
friend = ''
while friend.lower() != 'end':
    friend = str(input('Type the name of a friend: '))
    # add friends to list
    if friend != 'end':
        friends.append(friend)

# print friends
print()
print('Your friends are:')
for x in friends:
    print(x)


# 12 Prepare: Checkpoint
# Jaelee Hutchinson

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngestAge = 1000
youngestName = ''

for line in people:
    x = line.split()
    name = x[0]
    age = int(x[1])
    
    if age < youngestAge:
        youngestAge = age
        youngestName = name

print(f'The youngest person is {youngestName} with the age of {youngestAge}')
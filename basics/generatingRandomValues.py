import random

for i in range(3):
    print(random.randint(10, 20))

members = ['Mike', 'Mary', 'Bob', 'Justyna']
leader = random.choice(members)

print(leader)

import random
#print(dir(random))
#print(help(random.random))

#for i in range(10):
    #print(random.random())

# Generate a random number ranging from 3 to 7
    #Random, scale, shift, return...
"""
def myrandom():
    return 4 * random.random() + 3

for i in range(10):
    print(myrandom())


for i in range(10):
    print(random.uniform(5,9))


for i in range(20):
    print random.normalvariate(5, 1)

for i in range(5):
    print random.randint(1,6)
"""

game = ['rock', 'paper', 'scossors']
for i in range(10):
    print random.choice(game)

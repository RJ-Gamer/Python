import random

def random_walk(n):
    """ Returns the number of blocks after n block random walk"""
    x = 0
    y = 0

    for i in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])
        if step == 'N':
            y = y+1
        elif step =='S':
            y = y-1
        elif step == 'E':
            x = x+1
        else:
            x = x-1
    return(x,y)

for i in range(20):
    walk = random_walk(10)
    print(walk, "Distance from home = ",abs(walk[0]) + abs(walk[1]))

print(40* "*-")

def random_walk_fast(n):
    """ Returns the number of blocks after n block random walk"""
    x, y = 0,0
    for i in range(n):
        (dx, dy) = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
        x += dx
        y += dy
    return(x,y)

for i in range(20):
    walk = random_walk(10)
    print(walk, "Distance from home = ",abs(walk[0]) + abs(walk[1]))

number_of_walks = 50000

for walk_length in range(1, 31):
    no_transport = 0 #no. of walks 4 or less from home
    for i in range(number_of_walks):
        (x, y) = random_walk_fast(walk_length)
        Distance = abs(x) + abs(y)
        if Distance <= 4:
            no_transport += 1
    no_transport_percent = float(no_transport) / number_of_walks
    print("Walk size =", walk_length, "/% of no transport", 100*no_transport_percent)

"""squares = []
for i in range(1, 101):
    squares.append(i**2)

print squares
"""

"""
#### W THE LIST COMPREHENSIONS ####
print(40*"-!")
squares_List = [i**2 for i in range(1, 101)]
print squares_List

### Remainders

Remainders = [x**2 % 11 for x in range(1, 101)]
print Remainders
"""

name = [('Rajat',1994),('Rahul',1996), ('Sanket',1998), ('Sanjeev',2002), ('Yogesh',1994), ('Swapnil',1994), ('Sagar',1995), ('Ranjit',1997), ('Narsing',1965), ('Vivek',1989), ('Vaibhav',1994)]
before94 = [person for (person, year) in name if year < 1995]
print(before94)

"""
res = []
for person in name:
    if person.startswith("S"):
        res.append(person)

print res
res = [person for person in name if person.startswith("R")]
print res
"""

# Vector multiplication
vect = [3, -4, -1]
w = [6*x for x in vect]
print w

# Cartasion Product

A = [3, 5, 7, 11, 13]
B = [2, 4, 6, 8]

Cartasion_product = [(a,b) for a in A for b in B]
print Cartasion_product

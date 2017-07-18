""" DATA TYPES are SIX """
# NUMBERS
# STRINGS
# TUPLES
# LISTS
# DICTIONARY
# SETS

## LIST - Can be modified ... used with [ ]
pyList = ['Rajat', 'Shubham', 'Sanket']

# APPEND
pyList.append('Swapnil')
print(pyList)

#EXTEND
pyList.extend(['Suraj', 'Vaibhav'])
print(pyList)

#INSERT
pyList.insert(3, 'Arsh')
print(pyList)

#POP
pyList.pop()
print(pyList)


## DICTIONARY... used as key-value pair...{ }

myDictionary = {533:'Rajat', 532:['Diksha', 'priyanka'], 528:'Swapnil', 540:'Pooja', 538:'Vaibhav'}
print(myDictionary[528])

print(len(myDictionary)) #no. of key value pairs
print(myDictionary.keys()) # keys are printed
print(myDictionary.values()) #values are printed
print(myDictionary.items()) #saperate key-values pairs are printed
print(myDictionary.get(532)) #values at specified key are printed
myDictionary.update({581:'Mayuri'}) # adds key-values to the  DICTIONARY
print(myDictionary)


### SETS ####
# A set is an unordered collection of items
# Every element is unique and can not be changed
# Repeated values are shown just onces

firstSet = {'Rajat', 'Swapnil', 'Diksha', 'Pooja'}
secondSet = {'Rajat', 'Sanket', 'Shubham', 'Vaibhav'}
print(firstSet)

# OPERATIONS

# UNION
print(firstSet | secondSet)

# INTERSECTION
print(firstSet & secondSet)

# DIFFERENCE
print(firstSet - secondSet)
print(secondSet - firstSet)

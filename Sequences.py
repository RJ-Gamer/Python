subjects = ['Machine Learning', 'Internet and Cyber Security', 'Software Modelling and Design', 'Nusiness Intelligence', 'Cloud Computing']
languages = ['C', 'C++', 'Python', 'Java', 'JavaScript', 'HTML and CSS']

# append

subjects.append('Natural language Processing')
print(subjects)

#insert
languages.insert(3, 'Bootstrap')
print languages

#extend
languages.extend(['PHP', 'MongoDB'])
print languages

#remove
languages.remove('MongoDB')
print languages

#reverse
print subjects.reverse

 #concat
print subjects + languages

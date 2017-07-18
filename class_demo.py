class Student:
    def __init__(self, firstName, lastName, Rollno, marks):
        self.firstName = firstName
        self.lastName = lastName
        self.Rollno = Rollno
        self.marks = marks
        self.email = firstName.lower() + '.' + lastName.lower() + '@python.com'

    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def apply_raise(self):
        perc_rise = 1.05
        self.marks = float(self.marks * 1.05)

class Dump (Student):

    perc_rise = 1.10

    def __init__(self, firstName, lastName, Rollno, marks, prog_lang):
        super().__init__(firstName, lastName, Rollno, marks)
        self.prog_lang = prog_lang

#objStdFirst = Student('Rajat', 'Jog', 3154533, 84.91)
#objStdSecond = Student('Swapnil', 'Sapkal', 3154528, 93.54)

Rajat = Dump('Rajat', 'Jog', 3154533, 84.91, 'Python')
Swapnil = Dump('Swapnil', 'Sapkal', 3154528, 93.54, 'MongoDB')

#print objStdFirst.email

#print Rajat.marks
#dumbObjStdFirst.marks = dumbObjStdFirst.marks * Dump.perc_rise
#print dumbObjStdFirst.marks

print Rajat.firstName
print Swapnil.prog_lang
"""
# Get Help on Derieved Class
print(help(Dump))

objStdFirst.firstName = 'Rajat'
objStdFirst.lastName = 'Jog'
objStdFirst.Rollno = 3154533
objStdFirst.marks = 84.91

objStdSecond.firstName = 'Swapnil'
objStdSecond.lastName = 'Sapkal'
objStdSecond.Rollno = 3154528
objStdSecond.marks = 93.28
"""

"""
print(objStdFirst.email)
print(objStdSecond.email)
"""
#print('{} {}'.format(objStdFirst.firstName, objStdFirst.lastName))

"""
print(objStdFirst.fullname())
print(objStdSecond.fullname())

print(objStdFirst.marks)
objStdFirst.apply_raise()
print(objStdFirst.marks)

print(objStdSecond.marks)
objStdSecond.apply_raise()
print(objStdSecond.marks)
"""

"""
# Printing whole record
print objStdFirst.__dict__
print objStdSecond.__dict__

print Student.__dict__
"""

########## INHERITANCE ###########

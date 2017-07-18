class User:
    def __init__(self, full_name, birthday):
        """This function return name , lastname and birthdat of the user """
        self.name = full_name
        self.birthday = birthday

        # Extract the first and last names
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

"""
user = User("Rajat Jog", 19940212)
print user.name
print user.first_name
print user.last_name
print user.birthday
"""

help(User   )

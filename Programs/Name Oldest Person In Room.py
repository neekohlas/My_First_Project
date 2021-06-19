# Get list of of names and ages of people.  Return name of oldest person.

# Establish list variables
names_list = []
ages_list = []

# Get input of first name
name = input("Enter a person's name, or 'stop' to stop: ")

# While loop to stop process; gather age, add name and ages with .append, repeat name question.
while name != 'stop':
    age = int(input("What is the age of "+name+"? "))
    names_list.append(name)
    ages_list.append(age)
    name = input("Enter a person's name, or 'stop' to stop: ")

# Get max age from ages_list, then get position with index(). Set to age_max_pos.
age_max_pos = ages_list.index(max(ages_list))

print(names_list[age_max_pos], "is the oldest person in the room.")

# This is a final comment to test version control.

# name = input("What is your name? ")
# favorite_color = input("Enter your fave color ")
# print("hi " + name + " your fave color is " + favorite_color)

# birth_year = input("Enter your birthyear ")
# print(type(birth_year))
# age = 2022 - int(birth_year)
# print(age)
# print(type(birth_year))
# print(type(age))

# weight_lbs = input("Enter your weight in lbs: ")
# weight_kg = int(weight_lbs) * 0.45
# print(weight_kg)

# course = "Python' course for beginners"
# email_content = '''tripple quotes used for 
# multi-line strings
# '''
# print(course[0]) #gives the char of the first index
# print(course[-1]) #gives the char of the last index
# print(course[0:3]) #gives the chars from index 0 to 3, 3 exclusive output: Pyt
# print(course[:3]) #same thing, python assumes u want to start with 0, 0 to 3, 3 exclusive output: Pyt
# print(course[:]) #start index to end index => copies the string all together

# name = "0xkiichiro"
# print(name[1:-1])

# first = "baris"
# last = "aytimur"
# message = first + "[" + last + "] is a coder"
# msg = f"{first} [{last} is a coder]" # => f"" is used as prefix and combo with {} to write variables in strings!

## string methods

course = "python for beginners"
print(len(course)) # => len() for length of the string
print(course.upper())
print(course.lower())

print(course.find("P")) # => returns the first apperance index of the char. if it does not exist returns -1
print(course.replace("beginners", "absolute beginners")) # => replaces first with second

print("python" in course) # => this is a boolean expression meaning it will return true or false

# len() => find length of string
# course.upper() => convert uppercase
# course.lower() => convert lowercase
# course.title() => The title() method returns a string where the first character in every word is upper case.
# course.find() => finds first index of the char
# course.replace() => replaces chars
# "..." in course => bool expression if its in the string or not

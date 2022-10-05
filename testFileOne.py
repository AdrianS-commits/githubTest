# print("Hello World!")
# print("This is cool!!!")
# namefirst = input("Please enter your first name ")
# print("Your name is: " + namefirst.upper())

# now create a function to get your first name

def getInfo():
    """A function to get the user information from a user"""
    nameFirst = input("Please enter your first name, followed by enter ")
    nameLast = input("Please enter your last name, followed by enter ")
    return nameFirst, nameLast

def printInfo(g,h):
    """A function to print the users first and last name"""
    print("Hello, "+g.title() + " "+h.title())

def getAge():
    """Function to get the age of a user"""
    age = int(input("Please enter your age "))
    return age

def printAge(age):
    """A function to print the age"""
    print(age)

print("Welcome to File")

a,b = getInfo()
c = getAge()

printInfo(a,b)
printAge(c)

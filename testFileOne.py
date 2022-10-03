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

a,b = getInfo()

print("Welcome, " + a.title() + " " + b.title())

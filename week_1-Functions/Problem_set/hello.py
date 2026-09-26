'''#Ask users For their name
name = input("Enter Your name.")

#Remove any whitespace from the strings and also Capitalise the first letter
name = name.strip().title()

#Capitalist The name of String
#name = name.capitalize()

#Split the name of the person 
first, last = name.split(" ")

#Prnt hello and their name
print("Hello, \"Dude\"",last)

'''

def main():
    name = input("Enter your name: ")
    hello(name)

def hello(to):
    print("Hello," ,to )
main()



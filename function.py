#when you call a function, make sure the function is already defined, otherwise the interpreter will throw in an error

def hello(personName = "World"): #default parameter: incase the programmer doesn't specify a parameter when calling the function
    print("Hello", personName)

name = input("Enter your name: ")
hello()
hello(name)
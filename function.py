# when having user-defined functions, follow this order:
#   ->define your user function
#   ->define the main, where you call the user defined function(s)
#   ->call main()

def hello(personName = "World"): #default parameter: incase the programmer doesn't specify a parameter when calling the function
    print("Hello", personName)

def main():  
    name = input("Enter your name: ")
    hello(name)

main()
# Function called shout
# Accepts a string and returns it in uppercase with an exclamation mark
# main prompts the user for input, calls shout and prints the result

def shout(s):
    upperCased = s.upper()
    exclamation = f"{upperCased}", "!"
    return exclamation

def main():
    statement = input("What do you want to say? ")
    print(shout(statement))
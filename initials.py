# Prompt the user for their full name (Assume first and last name only, separated by a space)
# Implement a function called get_initials that accepts the full name as a str and returns the initials in UPPERCASE, formatted like "J.S.", with periods no spaces
# Call get_initials from main and print the result

def get_initials(n):
    firstInitial = n.split()[0][0]
    secondInitial = n.split()[1][0]
    initials = f"{firstInitial}.{secondInitial}.".upper()
    return initials

def main():
    personName = input("Enter your name: ")
    print(get_initials(personName))

main()
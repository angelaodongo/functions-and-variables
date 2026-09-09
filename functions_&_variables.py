# input
name = input("What is your name? ").strip().title()  

#Capitalize first letter of string
#name = name.capitalize()

#split user's name into first name and last name
first, last = name.split(" ")

# output
print (f"Hello, {first}")
# Implement a function called convert that accepts a temperature in Fahrenheit (as a float) and returns the equivalent in Celsius, rounded to 1 decimal place. 
# (Formula: C = (F - 32) * 5/9.) 
# Implement main, which prompts the user for a Fahrenheit temperature, calls convert, and prints the result formatted like "25.0 C".

def convert(C):
    C = float(C = (C - 32) * 5/9)
    return C

def main():
    fahrenheit = float(input("Enter degrees in Fahrenheit: "))
    print(f"{convert(fahrenheit):.1f}")
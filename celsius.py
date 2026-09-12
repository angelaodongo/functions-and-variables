# Implement a function called convert that accepts a temperature in Fahrenheit (as a float) and returns the equivalent in Celsius, rounded to 1 decimal place. 
# (Formula: C = (F - 32) * 5/9.) 
# Implement main, which prompts the user for a Fahrenheit temperature, calls convert, and prints the result formatted like "25.0 C".

def convert(F):
    C = (F - 32) * 5/9
    convertedValue = f"{float(C):.1f} C"
    return convertedValue

def main():
    fahrenheit = float(input("Enter degrees in Fahrenheit: "))
    print(convert(fahrenheit))

main()
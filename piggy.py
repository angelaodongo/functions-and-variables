# Implement a function called coins_to_dollars that accepts a number of coins (an int, assume all quarters, each worth 25 cents) 
# Returns the equivalent dollar amount as a float, formatted to 2 decimal places (e.g., 6 quarters → 1.50). 
# Implement main, which prompts the user for a number of coins, calls coins_to_dollars, and prints the result like "$1.50"

def coins_to_dollars(c):
    d = c * 0.25
    convertedValue = f"${float(d):.2f}"
    return convertedValue


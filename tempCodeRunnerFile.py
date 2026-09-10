def calculate(m):
    c = 300000000 
    E = m * c * c
    return E

def main():
    answer = int(input("Enter mass: "))
    print(f"{calculate(answer):,}", "J")

main()
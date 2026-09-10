def convert(f):
    f = f.replace(':)', '🙂').replace(':(', '🙁')
    return f

def main():
    phrase = str(input("Enter a phrase with emoji: "))
    print("->", convert(phrase))

main()
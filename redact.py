# Implement a function called redact that accepts a str sentence and a str word to redact, and returns the sentence with every occurrence of that word replaced by "[REDACTED]".
# Implement main, which prompts the user for a sentence and a word, calls redact, and prints the result.

def redact(s, w):
    s = s.replace(w, '[REDACTED]')
    return s

def main():
    sentence = input("Enter a phrase: ")
    word = input("What is the word you want redacted? ")
    print(redact(sentence,word))

main()
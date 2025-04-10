# manipulate.py

def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def remove_punctuation(s):
    import string
    return ''.join(char for char in s if char not in string.punctuation)

if __name__ == "__main__":
    print("Test: ", reverse_string("hello world!"))
    print("Capitalized: ", capitalize_words("hello world"))
    print("No punctuation: ", remove_punctuation("Hello, world!"))

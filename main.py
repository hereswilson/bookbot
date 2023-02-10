book_path = "books/frankenstein.txt"


def main():
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_report(num_words, chars_dict)

def get_book_text(path):
    with open(book_path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def print_report(num_words, chars_dict):
    char_list = [(char, chars_dict[char]) for char in chars_dict if char.isalpha()]
    char_list.sort(key=lambda a: a[1], reverse = True)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for char in char_list:
        print(f"The {char[0]} character was found {char[1]} times")

    print(f"--- End report ---")

main()

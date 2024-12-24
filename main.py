def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lower_string = make_string_lower(text)
    letter_dict = get_string_letters(lower_string)
    print(f"{num_words} words found in the document")
    print(f"The total letters by the alphabet are: {letter_dict}")
    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def make_string_lower(text):
    split_string = text.split()
    single_string = " ".join(split_string)
    all_lower = single_string.lower()
    return all_lower

def get_string_letters(string):
    alpha_dict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "j": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }
    for i in string:
        if i in alpha_dict:
            alpha_dict[i] += 1
    return alpha_dict

main()
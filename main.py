def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lower_string = make_string_lower(text)
    print(f"{num_words} words found in the document")
    


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

main()
def main():
    book_path = "books/frankenstein.txt"
    print_report(book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(book):
    num_words = len(book.split())
    return num_words

def get_char_count(book):
    book_lower = book.lower()
    char_dict = {}
    for char in book_lower:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def get_sorted_list(char_dict):
    sorted_list = []
    for ch in char_dict:
        sorted_list.append({"char": ch, "num":char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_report(path):
    text = get_book_text(path)
    num_words = get_word_count(text)
    char_dict = get_char_count(text)
    char_list = get_sorted_list(char_dict)
    print(f"--- Begin report of books/{path} ---" )
    print(f"{num_words} words found in the document")
    print()
    
    for pair in char_list:
        if pair["char"].isalpha():
            print(f"The '{pair["char"]}' character was found {pair["num"]} times")

    print('--- End report ---')

main()

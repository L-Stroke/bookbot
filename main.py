def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path) 
    word_count = count_words(text)
    char_counts = count_chars(text)
    char_counts_sorted = sort_dict(char_counts)
    generate_report(book_path, word_count, char_counts_sorted)

def count_words(string):
    words = string.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        f.close()
        return file_contents

def count_chars(string):
    all_lower = string.lower()
    unique_chars = {}
    for char in all_lower:
        if char in unique_chars:
            unique_chars[char] += 1
        else:
            unique_chars[char] = 1
    return unique_chars

def sort_dict(dictionary):
    list_of_dict = []
    for key in dictionary:
        list_of_dict += [{"char": key, "num": dictionary[key]}]

    list_of_dict.sort(reverse=True, key=lambda d: d["num"])
    return list_of_dict

def generate_report(path, total_words, character_totals):
    print(f"--- Begin report of {path} ---")
    print(f"{total_words} found in the document")
    print()
    
    for s in character_totals:
        if s['char'].isalpha():
            print(f"The '{s['char']}' character was found {s['num']} times")

    print("--- End report ---")

main()

def main():
    filepath = "books/frankenstein.txt"
    with open(filepath) as f:
        contents = f.read()
        word_count = get_word_count(contents)
        letter_count = get_letter_counts(contents)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        print()

        print_letter_count(letter_count)
        print("--- End report ---")


def get_word_count(text):
    return len(text.split())

def get_letter_counts(text):
    letters = {}
    
    for char in text.lower():
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1

    return letters

def convert_to_letter_list(dict):
    letters_list = []
    
    for letter in dict:
        if letter.isalpha():
            letters_list.append({ "letter": letter, "count": dict[letter]})
    
    return letters_list
    
def sort_on(dict):
    return dict["count"]

def print_letter_count(dict):
    letters_list = convert_to_letter_list(dict)
    
    letters_list.sort(reverse=True, key=sort_on)

    for entry in letters_list:
        print(f"The '{entry["letter"]}' character was found {entry["count"]} times")

main()

def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
        word_count = get_word_count(contents)
        print(f"Words: {word_count}")

        letter_count = get_letter_counts(contents)
        print(f"Letter count:")
        print(letter_count)


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


main()

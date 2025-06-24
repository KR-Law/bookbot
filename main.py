import sys
from stats import calc_words
from stats import calc_characters
from stats import sort_chars

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    text = get_book_text(path)
    num_words = calc_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    char_count = calc_characters(text)
    sorted_char = sort_chars(char_count)

    for char in sorted_char:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")   
    print("============= END ===============")
main()
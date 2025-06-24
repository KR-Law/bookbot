def calc_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def calc_characters(text):
    lower_text = text.lower()
    words = lower_text.split()
    char_count = {}

    for word in words:
        word_list = list(word)
        for char in word_list:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(char_list):
    return char_list["num"]

def sort_chars(char_dict):
    char_sort = []
    for char in char_dict:
        char_sort.append({"char": char, "num": char_dict[char]})
    char_sort.sort(reverse=True, key=sort_on)
    return char_sort



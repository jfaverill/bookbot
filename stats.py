def count_words(book_text):
    word_list = book_text.split()
    word_count = len(word_list)
    return word_count

def count_chars(book_text):
    char_dict = {}
    book_text = book_text.lower()
    for char in book_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_char_dict_list(char_dict):
    char_dict_list = []
    for key in char_dict:
        dict = {}
        dict["char"] = key
        dict["num"] = char_dict[key]
        char_dict_list.append(dict)
    char_dict_list.sort(key = sort_on, reverse = True)
    return char_dict_list


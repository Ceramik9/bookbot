def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_counter(file_path):
    words = get_book_text(file_path).split()
    return f"Found {len(words)} total words"

def character_counter(file_path):
    list_of_letters = list()
    dict_letters = dict()
    for letter in get_book_text(file_path):
        list_of_letters.append(letter.lower())
    for char in list_of_letters:
        if char not in dict_letters:
            dict_letters[char] = 1
        else:
            dict_letters[char] += 1
    return dict_letters

def refactor_dict(my_dict):
    new_dict = []
    for key in my_dict:
        new_dict.append({"character": key, "number": my_dict[key]})
    return new_dict

def sort_on(item):
    return item["number"]
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# word_counter - accepts file path and returns total word count
from stats import word_counter
total_word_count = word_counter(sys.argv[1])

# character_counter - accepts file path and returns total character count
from stats import character_counter
total_char_count = character_counter(sys.argv[1])

# refactor character counter to correct format
from stats import refactor_dict
new_character_count = refactor_dict(total_char_count)

# sort characters starting with highest number
from stats import sort_on
new_character_count.sort(reverse=True, key=sort_on)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(total_word_count)
    print("--------- Character Count -------")
    for character in new_character_count:
        print(f"{character["character"]}: {character["number"]}")
    print("============= END ===============")

main()


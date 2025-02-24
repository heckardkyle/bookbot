from stats import *
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_to_open = sys.argv[1]

    # read file and print report
    with open(file_to_open) as f:
        file_contents = f.read()

    print(f"--- Begin report of {file_to_open} ---")
    print(f"{word_count(file_contents)} words found in the document")
    print()

    character_list = char_count(file_contents)
    for character in character_list:
        print(f"{character['char']}: {character['num']}")
    
    print("--- End report ---")

main()
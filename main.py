from stats import *

def main():
    # read file and print report
    with open(file_to_open) as f:
        file_contents = f.read()

    print(f"--- Begin report of {file_to_open} ---")
    print(f"{word_count(file_contents)} words found in the document")
    print()

    character_list = char_count(file_contents)
    for character in character_list:
        print(f"The '{character['char']}' character was found {character['num']} times")
    
    print("--- End report ---")

file_to_open = "books/frankenstein.txt"

main()
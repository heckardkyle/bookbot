def word_count(file_contents):
    # return word count of file string
    word_count = file_contents.split()
    return len(word_count)

def sort_on(dict):
    return dict["num"]

def char_count(file_contents):
    # return list that counts occurence of each alpha character
    contents_lowered = file_contents.lower()

    character_dict = {}
    for character in contents_lowered:
        if (character not in character_dict) and (character.isalpha()):
            character_dict[character] = 1
        elif character.isalpha():
            character_dict[character] += 1

    character_list = []
    for key in character_dict:
        dict = {'char': key, 'num': character_dict[key]}
        character_list.append(dict)

    character_list.sort(key=sort_on, reverse=True)

    return character_list

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
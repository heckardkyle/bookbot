def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        print(word_count(file_contents))
        character_dict = char_count(file_contents)
        for character in character_dict:
            print(f"'{character}': {character_dict[character]}")

def word_count(file_contents):
    word_count = file_contents.split()
    return len(word_count)

def char_count(file_contents):
    contents_lowered = file_contents.lower()
    character_dict = {}
    for character in contents_lowered:
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1
    return character_dict


main()
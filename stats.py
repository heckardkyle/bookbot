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
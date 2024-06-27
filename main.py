def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = return_count(file_contents)
        char_dict = character_count(file_contents)
        sortie = list_sort(char_dict)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document.")
        print("\n")
        for x in sortie:
            if x['character'].isalpha():
                print(f"The {x['character']} character was found {x['count']} times")
        print("--- End report ---")


def return_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    char_count = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def list_sort(dict):
    list_dict = [{'character': key, 'count': value} for key, value in dict.items()]
    sorted_dict = sorted(list_dict, key=lambda x: x['count'], reverse=True)
    return sorted_dict


if __name__ == "__main__":
    main()
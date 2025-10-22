from stats import return_count, character_count, list_sort
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        with open(sys.argv[1]) as f:
            file_contents = f.read()
            word_count = return_count(file_contents)
            char_dict = character_count(file_contents)
            sortie = list_sort(char_dict)
            print("============ BOOKBOT ============")
            print("Analyzing book found at books/frankenstein.txt...")
            print("----------- Word Count ----------")
            print(f"Found {word_count} total words.")
            print("--------- Character Count -------")
            for x in sortie:
                if x['character'].isalpha():
                    print(f"{x['character']}: {x['count']}")
            print("--- End report ---")


if __name__ == "__main__":
    main()
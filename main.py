import sys
from stats import get_book_text, count_words, count_chars, sort_char_dict

def main():
    filepath = sys.argv[1]
    file_content = get_book_text(filepath)
    word_count = count_words(file_content)
    char_count = count_chars(file_content)
    print (f"Found {word_count} total words")
    print("--------- Character Count ------------")
    sorted_char_dict = sort_char_dict(char_count)
    for line in sorted_char_dict:
        print (str(line[0]) + ": " + str(line[1]))

    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main()
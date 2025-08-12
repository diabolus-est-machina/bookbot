from stats import get_book_text, count_words, count_chars

def main():
    filepath = "books/frankenstein.txt"
    file_content = get_book_text(filepath)
    word_count = count_words(file_content)
    char_count = count_chars(file_content)
    print (f"{word_count} words found in the document")
    print(char_count)
    


main()
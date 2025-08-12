from stats import get_book_text, count_words

def main():
    filepath = "books/frankenstein.txt"
    file_content = get_book_text(filepath)
    word_count = count_words(file_content)
    print (f"{word_count} words found in the document")


main()
def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content


def count_words(file_content):
    count = 0
    for word in file_content.split():
        count += 1
    return count


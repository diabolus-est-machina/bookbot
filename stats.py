def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content


def count_words(file_content):
    count = 0
    for word in file_content.split():
        count += 1
    return count

def count_chars(file_content):
    file_contents = file_content.lower()
    count_dict = {}
    for character in file_contents:
        if character.isalpha()==False:
            continue            
        if character not in count_dict:
            count_dict.update({character:1})
        else:
            count_dict.update({character:count_dict[character]+1})
    return(count_dict)

def sort_on(item):
    return item["num"]  # tell sort() to use the "num" value

def sort_char_dict(char_dict):
    char_list = list(char_dict.items())
    # Sort by the count (tuple index 1)
    char_list.sort(reverse=True, key=lambda item: item[1])
    return char_list
def main():
    path_to_file = "books/frankenstein.txt"

    file_contents = get_book_contents(path_to_file)
    words = get_word_count(file_contents)
    char_count = get_count_per_char(file_contents)
    char_list = [{"name": k, "num": v} for k, v in char_count.items()]
    filtered = [c for c in char_list if c["name"].isalpha()]
    filtered.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {path_to_file}  ---")
    print(f"{words} found in the document")
    print("\n")
    for item in filtered:
        print(f"The '{item['name']}' character was found {item['num']} times")
    print("--- End report ---")


def sort_on(dict):
    return dict["num"]


def get_count_per_char(content):
    char_dict = {}
    for char in content:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1

    return char_dict


def get_word_count(words):
    return len(words.split())


def get_book_contents(path_to_file):
    with open(path_to_file, "r") as file:
        file_contents = file.read()
    return file_contents


if __name__ == "__main__":
    main()

import requests

# suppose you want to see which author has a wider vocabulary
frankenstein = "https://www.gutenberg.org/ebooks/84.txt.utf-8"
dracula = "https://www.gutenberg.org/ebooks/345.txt.utf-8"


def count_words_in_book(book_url, book_name):
    """
    Count all the unique words inside the book
    :param book_name: The name that I want to use for the local copy of the book
    :param book_url: The url where the book is located
    :return: the number of unique words
    """
    r = requests.get(book_url)
    f = open(book_name, "wb")
    f.write(r.content)
    f.close()

# count_words_in_book(frankenstein, "frankenstein.txt")  - save a local copy

def count_unique_words(book):
    """
    Count the unique words inside the book
    :param book: Local filename for the book
    :return: The number of unique words
    """
    unique_words = set()
    punctuation = ".,;'?!_-\"<=>"
    total_words_count = 0
    f = open(book)
    for line in f:
        line = line.lower()
        for p in punctuation:
            line = line.replace(p, "")  # remove punctuation (',. etc) for the book
        words = line.split()
        # only counts words greater than 5:
        words = [w for w in words if len(w) > 5]  # w is short for "word"
        total_words_count += len(words)
        unique_words_in_line = set(words)  # this makes a set of all the words in the line (so only unique words)
        unique_words = unique_words.union(unique_words_in_line)  # (adding all the words)
    return len(unique_words), total_words_count


dracula_words, dracula_total_words = count_unique_words("dracula.txt")
frankenstein_words, frankenstein_total_words = count_unique_words("frankenstein.txt")
print(f"Dracula has {dracula_words} unique words vs Frankenstein that has {frankenstein_words} unique words")
print(f"Dracula has {dracula_total_words} unique words vs Frankenstein that has {frankenstein_total_words} unique words")
print(f"Dracula fraction: {dracula_words/dracula_total_words} vs Frankenstein fraction: {frankenstein_words/frankenstein_total_words}")

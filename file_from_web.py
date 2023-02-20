import requests

# locally copy the book from the web:

f = open("beyond the sunset", "w")
r = requests.get("https://www.gutenberg.org/cache/epub/70077/pg70077.txt")
# print(r.content) # Prints the book with bad encoding - \r \n \xe2 \ x80 etc - ascii
# print(r.content.decode()) # decodes the text
f.write(r.content.decode())
f.close()

f = open("beyond the sunset2", "wb")  # as a byte string
r = requests.get("https://www.gutenberg.org/cache/epub/70077/pg70077.txt")
# print(r.content) # Prints the book with bad encoding - \r \n \xe2 \ x80 etc - ascii
# print(r.content.decode()) # decodes the text
f.write(r.content) # decodes the text
f.close()

# count how many times the letter "a" shows in the book
num_a = 0
f = open("beyond the sunset2")
for line in f:
    num_a += line.count("a")
print(f"The number of times 'a' shows up in the book is {num_a}")

# cound the number of words in the book
f = open("beyond the sunset2")
num_words = 0
for line in f:
    words = line.split()
    num_words += len(words)

print(f"In the book there are {num_words} words")


f = open("text.txt", "r")  # opening for reading is the default way

# print(f.read()) # read will give you all the information inside the file

# next we read it line by line. The file descriptor is iterable

for line in f:
    # there is a new line in the text file and also print adds a new line, so that is why we have double new lines
    print(f"line: {line}", end = "") # adding end removes the \n new line after each line
    print(f"line: {line.rstrip()}")





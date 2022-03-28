def open_file(filename):
    file = open(filename, "r")
    lines = file.readline()
    return lines

def main():
   file_lines = open_file("warpiece.txt")
   word_count(file_lines)


def display_results(word_counts):
    for word in word_counts:
        count = word_counts(word)
        print(f"{word}: t/ {count}")



def word_count(all_lines):
    word_counter = {}
    for line in all_lines:
        words_in_line = line.split(" ")
        for word in words_in_line:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word]=1

    return word_counter




main()

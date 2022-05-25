# Read text from a file, and count the occurence of words in that text

def read_file_content(filename):
    # [assignment] Add your code here
    f = open(filename, 'r')
    return f


def count_words():
    text = read_file_content("./story.txt")

    word_dic = dict()

    for line in text:
        line = line.rstrip()
        line = line.split()
        # print(line)
        for word in line:
            word_dic[word] = word_dic.get(word, 0) + 1

    print(word_dic)


count_words()

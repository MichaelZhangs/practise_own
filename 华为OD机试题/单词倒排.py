import re


def word_sort():
    while True:
        try:
            s = input()
            sp_word = re.split('[^a-zA-Z]+', s)
            print(sp_word)
            print(" ".join(sp_word[::-1]).strip())
        except:
            break


word_sort()

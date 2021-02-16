STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    with open(file) as praise_song:
        words = praise_song.read()
        words = words.lower()
        words_list = words.split(' ')
        words_list_copy = words_list.copy()
        for word in words_list_copy:
            for stop in STOP_WORDS:
                if stop == word:
                    words_list_copy.remove(word)
    print(words_list_copy)




    #pass



if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

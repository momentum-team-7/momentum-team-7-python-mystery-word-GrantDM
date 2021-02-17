STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    with open(file) as praise_song:
        words = praise_song.read()
        words = words.lower()
        words_count_list = {}

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for ele in words:
            if ele in punctuations:
                words = words.replace(ele, "")
                words = words.replace("\n", " ")

        words_list = words.split()
        words_list_copy = words_list.copy()
        for word in words_list:
            if word in STOP_WORDS:
                words_list_copy.remove(word)
            elif word not in words_count_list:
                temp_count = words_list_copy.count(word)
                words_count_list[word] = temp_count

        sorted_values = sorted(words_count_list.values(), reverse = True)
        sorted_dict = {}

        for index in sorted_values:
            for key in words_count_list.keys():
                if words_count_list[key] == index:
                    sorted_dict[key] = words_count_list[key]

        for key in sorted_dict:
            print( key, ':', sorted_dict[key])

        # words_count_list = sorted(words_count_list, key=words_count_list.get)
        print(words_list_copy)
        # print(sorted_dict)
        
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

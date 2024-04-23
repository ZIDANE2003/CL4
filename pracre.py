# # import re
# # from multiprocessing import Pool

# # WORD_RE = re.compile(r"[\w']+")

# # def read_file(file_name):
# #     with open(filename, 'r') as file:
# #         return file.readlines()

# # def reducer(mapped_counts):
# #     reduced_counts = {}
# #     for word_count in mapped_counts:
# #         for word, count in word_count.items():
# #             reduced_counts[word] = reduced_counts.get(word, 0) + count
# #             print(reduced_counts)
# #             return reduced_counts



# # def main(filename, target_word):
# #     lines = read_file(filename)
# #     with Pool() as pool:
# #         mapped_counts = pool.map(mapper, lines)
# #     reduced_counts = reducer(mapped_counts)

# # # Get the frequency of the target word
# #     target_frequency = reduced_counts.get(target_word.lower(), 0)
# #     print(f"The frequency of '{target_word}' in the file is: {target_frequency}")

# # if __name__ == "__main__":
# #     filename = input("Enter the file name: ")
# #     target_word = input("Enter the word to find frequency: ")
# #     main(filename, target_word)


# import re
# from multiprocessing import Pool

# WORD_RE = re.compile(r"[\w']+")

# def read_file(file_name):
#     with open(file_name, 'r') as file:
#         return file.readlines()

# def mapper(line):
#     return WORD_RE.findall(line)

# def reducer(mapped_counts):
#     reduced_counts = {}
#     for word_count in mapped_counts:
#         for word, count in word_count.items():
#             reduced_counts[word] = reduced_counts.get(word, 0) + count
#     return reduced_counts

# def main(filename, target_word):
#     lines = read_file(filename)
#     with Pool() as pool:
#         mapped_counts = pool.map(mapper, lines)
#     reduced_counts = reducer(mapped_counts)

#     # Get the frequency of the target word
#     target_frequency = reduced_counts.get(target_word.lower(), 0)
#     print(f"The frequency of '{target_word}' in the file is: {target_frequency}")

# if __name__ == "__main__":
#     filename = input("Enter the file name: ")
#     target_word = input("Enter the word to find frequency: ")
#     main(filename, target_word)

import re
from multiprocessing import Pool
from collections import defaultdict

WORD_RE = re.compile(r"[\w']+")

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

def mapper(line):
    word_counts = defaultdict(int)
    words = WORD_RE.findall(line)
    for word in words:
        word_counts[word.lower()] += 1
    return word_counts

def reducer(mapped_counts):
    reduced_counts = defaultdict(int)
    for word_count in mapped_counts:
        for word, count in word_count.items():
            reduced_counts[word] += count
    return reduced_counts

def main(filename, target_word):
    lines = read_file(filename)
    with Pool() as pool:
        mapped_counts = pool.map(mapper, lines)
    reduced_counts = reducer(mapped_counts)

    # Get the frequency of the target word
    target_frequency = reduced_counts.get(target_word.lower(), 0)
    print(f"The frequency of '{target_word}' in the file is: {target_frequency}")

if __name__ == "__main__":
    filename = input("Enter the file name: ")
    target_word = input("Enter the word to find frequency: ")
    main(filename, target_word)






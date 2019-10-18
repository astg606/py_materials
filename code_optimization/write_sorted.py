"""Sorting a large, randomly generated string and writing it to disk"""
import random


def write_sorted_letters(nb_letters=10**7):
    random_string = ''
    for i in range(nb_letters):
        random_string += random.choice('abcdefghijklmnopqrstuvwxyz')
    sorted_string = sorted(random_string)

    with open("sorted_text.txt", "w") as sorted_text:
         for character in sorted_string:
             sorted_text.write(character)

if __name__ == '__main__':
   write_sorted_letters()

#!/usr/bin/env python3
# HW08_ch11_ex02b
# This borrows from exercise two in the book.
# Dictionaries have a method called keys that returns the keys of the
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical
# order.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
###############################################################################
# Imports


# Body
def print_hist_old(dictionary):
    print(sorted(list(dictionary.items()))) #since a dict doesn't have any order, i converted it to the list of tuples


def print_hist_new(h):
    pass


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################

pledge_histogram = {}


def histogram_old(lst):
    d = {word:0 for word in lst}
    for word in lst:
    #    if word not in d:
    #        d[word] = 1
    #    else:
    #        d[word] += 1 
       d.get(word, 0)
       d[word] +=1
    return d


def histogram_new(lst):
        pledge_histogram = histogram_old(lst)
        return pledge_histogram


def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. returns the list.
    """
    with open('pledge.txt', 'r') as f:
        pledge_list = f.read().lower().split()

    return pledge_list

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def main():
    """ Calls print_hist_new with the appropriate arguments to print the
    histogram of pledge.txt.
    """
    print_hist_old(histogram_old(get_pledge_list()))

if __name__ == '__main__':
    main()

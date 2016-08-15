#!/usr/bin/env python3
# HW08_ch11_ex02c.py
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
###############################################################################
# Imports


# Body
def reverse_lookup_old(dic, val):
    key_list = []
    for k, v in dic.items():
        if str(v) == val:
            key_list.append(k)
        else:
        	continue
    return key_list


def reverse_lookup_new(d, v):
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
#    with open('pledge.txt', 'r') as f:
#        words = f.read().split()
        pledge_histogram = histogram_old(lst)
        return pledge_histogram


def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. returns the list.
    """
    with open('pledge.txt', 'r') as f:
        pledge_list = f.read().split()
    return pledge_list


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def main():   # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    print(reverse_lookup_old(pledge_histogram, "1"))
    print(reverse_lookup_old(pledge_histogram, "9"))
    print(reverse_lookup_old(pledge_histogram, "Python"))

if __name__ == '__main__':
    main()

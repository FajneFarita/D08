#!/usr/bin/env python3
# HW08_ch11_ex02d.py
# (1) Write a more concise version of invert_dict_old.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Update print_hist_new from HW08_ch11_ex02b.py to be able to print
# a sorted version of the dict (print key/value pairs from 0 through the
# largest key values, (and those in between))
# Ex. If d = {1:["this, that"], 3: ["the"]}, it prints:
#    '1: ["this", "that"]'
#    '2:'
#    '3: ["the"]'
###############################################################################
# Imports


# Body
def invert_dict_old(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def invert_dict_new(d):
    new_d = {}
    for k, v in d.items():
        new_d[v] = new_d.get(v, [])
        new_d[v].append(k)
    return new_d



def print_hist_newest(d):
    lis = list(d.keys())
    for i in (range(1, lis[-1]+1)):
        if i in list(d.keys()):
            print(str(i) + ": " + str(d[i]))
        else:
            print(str(i) + ": ")


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
        pledge_list = f.read().lower().split()
    return pledge_list


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def main():  # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    pledge_invert = invert_dict_new(pledge_histogram)
    print_hist_newest(pledge_invert)

if __name__ == '__main__':
    main()

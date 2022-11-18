'''This script converts the RNA sequences back to DNA'''
import sys

def converter(in_seq):
    out_seq = ''
    in_seq = in_seq.upper() #control for lowercase
    for letter in in_seq:
        if letter == 'U':
            out_seq += 'T'
        else:
            out_seq += letter
    return print ( '\n' + out_seq)

converter(sys.argv[1])

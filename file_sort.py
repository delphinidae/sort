#!/usr/bin/python3
import os
import file_operations
import argparse
#import functools


def split_list(c):
    ll = len(c)
    a = c[:int(ll / 2)]
    b = c[int(ll / 2):]
    #print("list a: {0}".format(a))
    #print("list b: {0}".format(b))
    return a, b


file_counter = 0
files_list = []

parser = argparse.ArgumentParser()
parser.add_argument('-i', dest='input', default='input', help='input file path')
parser.add_argument('-o', dest='output', default='output', help='output file path')
parser.add_argument('-m', dest='max_size', default=90 * 1000 * 1000, help='max size of avaliable memory')
args = parser.parse_args()
file_name_in = args.input
mem_size = int(args.max_size) * 0.7
file_size = os.path.getsize(file_name_in)

file_counter = file_operations.split_files(file_name_in, files_list, mem_size)

print ("We have {0} sorted files".format(file_counter))

file_one = files_list[0]
tmp_name_out = files_list[-1]

#tmp_name_out = functools.reduce(lambda a, x: file_operations.merge_files(a, x), files_list)
while len(files_list) > 1:
    a, b = split_list(files_list)
    files_list = []
    for i in range(len(a)):
        files_list.append(file_operations.merge_files(a[i], b[i]))
    if len(b) > len(a):
        files_list.append(b[-1])
tmp_name_out = files_list[0]
os.rename(tmp_name_out, args.output)

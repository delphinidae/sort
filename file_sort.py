#!/usr/bin/python3
import os
import file_operations
import argparse


file_counter = 0
files_list = []

parser = argparse.ArgumentParser()
parser.add_argument('-i', dest='input', default='input', help='input file path')
parser.add_argument('-o', dest='output', default='output', help='output file path')
args = parser.parse_args()
file_name_in = args.input
file_size = os.path.getsize(file_name_in)

file_counter = file_operations.split_files(file_name_in, files_list)

print ("We have {0} sorted files".format(file_counter))

#file_one = file_name_in + '_sorted_{0}'.format(1)
file_one = files_list[0]
tmp_name_out = files_list[-1]
for i in range(1, file_counter):
    file_two = files_list[i]
    tmp_name_out = 'sorted-{0}-{1}'.format(i, i + 1)
    #print ("File 1: {0}, file 2: {1}, out: {2}".format(file_one, file_two, tmp_name_out))
    if file_operations.merge_files(file_one, file_two, tmp_name_out):
        os.remove(file_one)
        os.remove(file_two)
        file_one = tmp_name_out
    else:
        raise Exception('Failed to merge files')

os.rename(tmp_name_out, args.output)

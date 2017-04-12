#!/usr/bin/python3
import argparse
import random

def random_text(length):
    rs = ""
    for i in range(0, length):
        rs = rs + random.choice('abcdef0123456789')
    return rs

parser = argparse.ArgumentParser()
parser.add_argument('-i', dest='input', default='input', help='input file path')
parser.add_argument('-n', dest='num', default=10000, help='number of iterations')
parser.add_argument('-l', dest='line', default=100, help='line length')
args = parser.parse_args()
file_name_in = args.input
n = int(args.num)
l = int(args.line)
f = open(file_name_in, "w")

#generate the content
for line in range(n):
    f.write(random_text(l))
    f.write("\n")
print ("File size: {0}".format(l*n))
f.close()


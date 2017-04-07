#!/usr/bin/python3
import argparse
import random_crap
import random

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
    f.write(random_crap.random_text(l))
    f.write("\n")
print ("File size: {0}".format(l*n))
"""
for x in range(9400000):
    f.write(str(random.randint(1000000, 2000000)))
    f.write("\n")
"""
f.close()


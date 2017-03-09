#!/usr/bin/python3

import random_crap
import random

f = open("input", "w")

#generate the content
#for line in range(100000):
#    f.write(random_crap.random_text(100))
#    f.write("\n")

for x in range(1000000):
    f.write(str(random.randint(1000000, 2000000)))
    f.write("\n")
f.close()


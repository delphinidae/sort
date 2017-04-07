#!/bin/bash
for i in 100 1000 10000 100000 1000000
do
python3 generate_large_file.py -n $i
echo "Printed lines: "
python3 file_sort.py -m 1000 | grep LINE |wc -l
done
exit 0

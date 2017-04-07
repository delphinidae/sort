func()
{
echo "Current conditions: lines -- $1, iterations -- $2, max_size -- $3"
python3 generate_large_file.py -l $1 -n $2
python3 file_sort.py -m $3
sort input > syssort
diff output syssort
}

func 100 500 1000
func 100 3 580
func 100 15 580

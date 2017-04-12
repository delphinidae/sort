func()
{
echo "Current conditions: lines -- $1, iterations -- $2, max_size -- $3"
python3 generate_large_file.py -l $1 -n $2
if python3 file_sort.py -m $3; then
echo "Perfoming system sort"
sort input > syssort
diff output syssort
echo "Done"
rm syssort
fi
rm input
}

func 100 500 1000
func 100 3 580
func 100 3 500
func 100 15 580
func 100 100000 1000
func 100 100000 10000
func 100 100000 100000
func 100 100000 1000000

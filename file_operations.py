import os


def merge_files(file_name1, file_name2, file_name_out="temp_file_out"):
    with open(file_name1, 'r') as f1:
        with open(file_name2, 'r') as f2:
            with open(file_name_out, 'w') as f_out:
                l1 = f1.readline()
                l2 = f2.readline()

                while True:
                    #print("l1: {0}, l2: {1}".format(l1, l2))
                    if l1 == '':
                        #the first file has come to the end
                        if l2 != '':
                            f_out.write(l2)
                        for rest_l2 in f2:
                            f_out.write(rest_l2)
                        break
                    if l2 == '':
                        if l1 != '':
                            f_out.write(l1)
                        #the second file has come to the end
                        for rest_l1 in f1:
                            f_out.write(rest_l1)
                        break
                    if l1 < l2:
                        f_out.write(l1)
                        l1 = f1.readline()
                    elif l1 == l2:
                        f_out.write(l1)
                        f_out.write(l2)
                        l1 = f1.readline()
                        l2 = f2.readline()
                    else:
                        f_out.write(l2)
                        l2 = f2.readline()

    os.remove(file_name1)
    os.remove(file_name2)
    os.rename(file_name_out, file_name2)
    #print ("file 1: {0}, file 2: {1}, file out: {1}".format(file_name1, file_name2))
    return file_name2


def sort_file(file_counter, line_list, files_list, file_name_in):
    line_list.sort()
    new_file_name = file_name_in + '_sorted_{0}'.format(file_counter)
    files_list.append(new_file_name)
    with open(new_file_name, 'w') as f:
        for out_string in line_list:
            f.write(out_string)
    #print("We ave written new file: {0}".format(new_file_name))


def split_files(file_name_in, files_list, max_size=40 * 1000 * 1000):
    processed_size = 0
    file_counter = 0
    line_list = []
    with open(file_name_in, 'r') as f_in:
        for input_line in f_in:
            if len(input_line) >= max_size / 4:
                raise Exception("Line is too long!")
            processed_size += len(input_line)
            line_list.append(input_line)
            if processed_size >= max_size:
                file_counter += 1
                sort_file(file_counter, line_list, files_list, file_name_in)
                line_list = []
                processed_size = 0
    # the rest...
    if len(line_list) > 0:
        file_counter += 1
        sort_file(file_counter, line_list, files_list, file_name_in)
    return file_counter

''' WAP to accept a name of a file from user  and print count of lines present in that file based on following filters
 if filter comes as empty string, then total line count
 if filter comes as ^input_string, count only those lines which begins with input_string.
 if filter comes as input_string$, count only those lines which ends wih hello
 if filter comes as input_string, count those lines which contains input_string.
'''

def line_filter(fd):

    input_string = input("Enter string : ")

    if input_string == "":
        cnt = 0
        line = fd.readline()
        while line != "":
            cnt = cnt + 1
            line = fd.readline()

        return cnt

    elif "^" in input_string:
        filter_string = input_string[1:]
        filter_string = filter_string.lower()
        start_cnt = 0
        line = fd.readline()
        while line != "":
            line = line.lower()
            if line.startswith(filter_string):
                start_cnt = start_cnt + 1
            line = fd.readline()

        return start_cnt

    elif "$" in input_string:
        filter_string = input_string[:-1]
        filter_string = filter_string.lower()
        end_cnt = 0
        line = fd.readline()
        while line != "":
            line.strip()
            line = line.lower()
            if line.endswith(filter_string + "\n"):
                end_cnt = end_cnt + 1
            line = fd.readline()

        return end_cnt

    elif input_string != "":
        contains_cnt = 0
        line = fd.readline()
        while line != "":
            if input_string in line:
                contains_cnt = contains_cnt + 1
            line = fd.readline()

        return contains_cnt


def main():
    file_name = input("Enter file name to open :")
    fd = open(file_name)
    count = line_filter(fd)
    print("Filtered line count :", count)


if __name__ == '__main__':
    main()

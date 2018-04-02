# WAP to accept a name of file and pattern to be search at beginning.
# Write a generator which returns the lines which matching the given pattern.


import re


def pattern_matching_use_gene(fd):
    pattern = input("Enter pattern:")
    pattern = "^" + pattern
    line = fd.readline()
    print("Lines which are matching pattern:")
    while line != "":

        if line != "":
            ans = re.search(pattern, line, re.IGNORECASE)
            if ans:
                yield line
        line = fd.readline()


def main():
    file_name = input("Enter file name to open:")
    fd = open(file_name)

    result = pattern_matching_use_gene(fd)
    
    for line in result:
        print(line)


if __name__ == '__main__':
    main()

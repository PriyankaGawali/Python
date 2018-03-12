# WAP using list comprehension which returns intersection of two lists


def main():
    l1 = [1, 9, 5, 4, 3]
    l2 = [4, 9, 3, 2, 1]
    print([x for x in l1 if x in l2])


if __name__ == '__main__':
    main()

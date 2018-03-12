# WAP to print unique elements from list


def is_unique(list_a):
    i = 0
    ans_list = []
    while i < len(list_a):
        count = 0
        for x in list_a:
            if x == list_a[i]:
                count = count + 1

        if count == 1:
            ans_list.append(list_a[i])

        i = i + 1

    return ans_list


def main():
    l1 = [1, 3, 4, 7, 2, 3, 11, 1]
    l2 = is_unique(l1)
    print(l2)


if __name__ == '__main__':
    main()

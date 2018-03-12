# WAP to accept 2 lists from user . Sort them without using built in sort() method and then merge the two sorted list.


def sort_list(list_a):
    len_list = len(list_a)
    for i in range(0, len_list):
        for j in range(i + 1, len_list):
            if list_a[i] > list_a[j]:
                temp = list_a[i]
                list_a[i] = list_a[j]
                list_a[j] = temp


def merge_lists(l1, l2):

    ans_list = []

    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            ans_list.append(l1[i])
            i = i + 1
        else:
            ans_list.append(l2[j])
            j = j + 1

  
    if i < len(l1):
        ans_list.extend(l1[i:])

    if j < len(l2):
        ans_list.extend(l2[j:])

    return ans_list


def main():
    list_a = [6, 4, 10, 1, 9]
    list_b = [8, 11, 5, 20]
    sort_list(list_a)
    sort_list(list_b)
    print(list_a)
    print(list_b)
    print("After sort and merge : ", merge_lists(list_a, list_b))


if __name__ == '__main__':
    main()

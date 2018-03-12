# Implement set functions on list
# union
# Intersection
# symmetric_difference
# difference
# disjoint
# issuperset
# issubset


import sys


def union_of_lists(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    return list(set_a.union(set_b))


def intersection_of_lists(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    return list(set_a.intersection(set_b))


def difference_of_lists(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    return list(set_a.difference(set_b))


def symmetric_diff_of_lists(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    return list(set_a.symmetric_difference(set_b))


def is_disjoint(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    return set_a.isdisjoint(set_b)


def is_superset(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    return set_a.issuperset(set_b)


def is_subset(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    return set_a.issubset(set_b)


def main():
    # accept 2 lists from user
    list_a = eval(input('Enter list here: '))
    list_a = list(list_a)
    print(list_a)

    list_b = eval(input('Enter list here: '))
    list_b = list(list_b)
    print(list_b)

    while True:
        print("Menu")
        print("1. Union")
        print("2. Intersection")
        print("3. Difference")
        print("4. Symmetric difference")
        print("5. Is disjoint")
        print("6. Is superset")
        print("7. Is subset")
        print("8. Exit")
        choice = int(input("Enter choice : "))

        if choice == 1:
            print("Union : ", union_of_lists(list_a, list_b))

        elif choice == 2:
            print("Intersection : ", intersection_of_lists(list_a, list_b))

        elif choice == 3:
            print("Difference : ", difference_of_lists(list_a, list_b))

        elif choice == 4:
            print("Symmetric difference : ", symmetric_diff_of_lists(list_a, list_b))

        elif choice == 5:
            print("list_a is disjoint with list_b : ", is_disjoint(list_a, list_b))

        elif choice == 6:
            print("list_a is super set of list_b : ", is_superset(list_a, list_b))

        elif choice == 7:
            print("list_a is subset of list_b : ", is_subset(list_a, list_b))

        elif choice == 8:
            sys.exit()

        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()

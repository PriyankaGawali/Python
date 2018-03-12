# WAP to implement a stack  using list

import sys


def is_empty(list_a):
    if len(list_a) == 0:
        return 1


def is_full(list_a):
    if len(list_a) == 10:
        return 1


def push(list_a, data):
    if is_full(list_a):
        print("List is full")
    else:
        if type(list_a) == type(data):
            list_a.extend(data)
        else:
            list_a.append(data)


def pop(list_a):
    if is_empty(list_a):
        print("List is empty")
    else:
        list_a.pop()


def main():
    list_a = [1,2,3,4]
    while True:
        print("Menu")
        print("1. Push")
        print("2. Pop")
        print("3. Exit")
        choice = int(input("Enter choice : "))
        if choice == 1:
            data = input("Enter data to append : ")
            push(list_a, data)
            print(list_a)

        elif choice == 2:
            pop(list_a)
            print(list_a)

        elif choice == 3:
            sys.exit()

        else:
            print("Invalid choice")




if __name__ == '__main__':
    main()

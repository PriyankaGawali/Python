# WAP to implement queue using list
# FIFO
# IsQueueEmpty
# IsQueueFull
# EnQueue- insert
# Dequeue - remove

import sys


def is_que_full(list_a):
    if len(list_a) == 10:
        return 1


def is_que_empty(list_a):
    if len(list_a) == 0:
        return 1


def enqueue(list_a,data):
    if is_que_full(list_a):
        print("List is full")
    else:
        if type(list_a) == type(data):
            list_a.extend(data)
        else:
            list_a.append(data)


def dequeue(list_a):
    if is_que_empty(list_a):
        print("List is empty")
    else:
        list_a.pop(0)


def main():
    list_a = [1, 2, 3, 4]
    while True:
        print("Menu")
        print("1. Check whether queue is full")
        print("2. Check whether queue is empty")
        print("3. En-queue")
        print("4. De-queue")
        print("5. Exit")
        choice = int(input("Enter choice : "))
        if choice == 1:
            if is_que_full(list_a):
                print("List is full")
            else:
                print("List is not full")

        elif choice == 2:
            if is_que_empty(list_a):
                print("List is empty")
            else:
                print("List is not empty")

        elif choice == 3:
            data = input("Enter data to append :")
            enqueue(list_a, data)
            print(list_a)

        elif choice == 4:
            dequeue(list_a)
            print(list_a)

        elif choice == 5:
            sys.exit()

        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()


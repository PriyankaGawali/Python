# WAP to implement stack using class

import sys


class Stack:

    def __init__(self, size = 5):
        self.size = size
        self.list_a = []

    def is_empty(self):
        if len(self.list_a) == 0:
            return True
        return False

    def is_full(self):
        if len(self.list_a) == self.size:
            return True
        return False

    def push(self, value):
        if self.is_full():
            print("Stack is full")
        else:
            self.list_a.append(value)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Pop value : ", self.list_a.pop())


def main():
    stack_obj = Stack()
    while True:
        print("1. Check whether stack is empty")
        print("2. Check whether stack is full")
        print("3. Add element to stack")
        print("4. Remove element from stack")
        print("5. Exit")
        choice = input("Enter choice :")
        if choice == "1":
            if stack_obj.is_empty():
                print("Stack is empty")
            else:
                print("Stack is not empty")

        elif choice == "2":
            if stack_obj.is_full():
                print("Stack is full")
            else:
                print("Stack is not full")

        elif choice == "3":
            value = input("Enter value to add :")
            stack_obj.push(value)

        elif choice == "4":
            stack_obj.pop()

        elif choice == "5":
            sys.exit()

        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()

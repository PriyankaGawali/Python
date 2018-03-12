# WAP to accept directory path from user and accept file of types to be deleted recursively from the given directory

import os


def delete_files(user_input):
        file_extension = input("Enter type of files to delete :")

        for root, dirs, files in os.walk(user_input):
            for current_file in files:
                if current_file.lower().endswith(file_extension):
                    os.remove(os.path.join(root, current_file))

        print("Files are deleted successfully")


def main():
    user_input = input("Enter directory path :")
    if os.path.exists(user_input):
        delete_files(user_input)
    else:
        print("Invalid path")


if __name__ == '__main__':
    main()

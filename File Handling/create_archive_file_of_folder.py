# WAP to create an archive file of the specified folder using sh util module.


import shutil


def main():
    folder_name = input("Enter folder name to create an archive :")
    file_format = input("Enter file format zip or tar format :")
    output_file_name = input("Enter output file name : ")

    # shutil.make_archive(output_filename, 'zip', dir_name)
    shutil.make_archive(output_file_name, file_format,folder_name)


if __name__ == '__main__':
    main()

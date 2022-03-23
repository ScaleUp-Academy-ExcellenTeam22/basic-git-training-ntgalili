
import os


def file_start(path :str,start:str):
    """
    the function get a path of a directory and find the files in the directory that start with start
    :param path: the path of the directory
    :param start: the str that the file's names start with
    :return: list of files
    """

<<<<<<< HEAD
    list_of_files = os.listdir(path) # get the list of the files in the directory
    starts_files = [file for file in list_of_files if file.startswith(start)] # get the list of the files that start with start
=======
    list_of_files = os.listdir(path)  # get the list of the files in the directory
    starts_files = [f for f in list_of_files if f.startswith(start)] # get the list of the files that start with start
>>>>>>> 94c4a663d55bac3d77548b93a2ecd32048e05822
    return starts_files

def main():
    path = input("Enter a path of directory: ")
    deep_file = file_start(path,'deep') # find the files in the directory that start with 'deep'
    print(deep_file)


if __name__ == "__main__":
    main()

# lib/file_io.py

def write_file(file_name, file_content):
    """
    Write content to a .txt file, overwriting any existing content.
    """
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)


def append_file(file_name, file_content):
    """
    Append content to a .txt file.
    """
    with open(f"{file_name}.txt", "a") as file:
        file.write(file_content)


def read_file(file_name):
    """
    Read and return the content of a .txt file.
    """
    with open(f"{file_name}.txt", "r") as file:
        return file.read()

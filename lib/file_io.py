def write_file(file_name, file_content):
    """
    Write content to a text file.

    Args:
        file_name (str): The name of the file (including file extension).
        file_content (str): The content to be written to the file.
    """
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)


def append_to_file(file_name, append_content):
    """
    Append content to an existing text file.

    Args:
        file_name (str): The name of the file (including file extension).
        append_content (str): The content to be appended to the file.
    """
    with open(f"{file_name}.txt", "a") as file:
        file.write(append_content)


def read_file(file_name):
    """
    Read content from a text file.

    Args:
        file_name (str): The name of the file (including file extension).

    Returns:
        str: The content read from the file.
    """
    with open(f"{file_name}.txt", "r") as file:
        return file.read()

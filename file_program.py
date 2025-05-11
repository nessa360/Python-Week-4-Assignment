# # QUestion: 1
# # Create a program that reads a file and writes a modified version to a new file.
from sqlite3.dbapi2 import Timestamp


def read_file(file_path):
    """
    Reads the content of a file and returns it as a string.
    
    :param file_path: Path to the file to be read.
    :return: Content of the file as a string.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None     
def write_file(file_path, content):
    """
    Writes the given content to a file.
    
    :param file_path: Path to the file to be written.
    :param content: Content to be written to the file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Content successfully written to {file_path}.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
def modify_content(content):
    """
    Modifies the content by converting it to uppercase.
    
    :param content: Original content of the file.
    :return: Modified content.
    """
    return content.upper() + " I love coding!"
def get_filename_from_user():
    """
    Prompts the user to enter the name of the input file.
    
    :return: The file name entered by the user.
    """
    return input("Please enter the name of the input file: ")

def main():
    input_file = get_filename_from_user()  # Ask user for the input file
    output_file = 'output.txt'  # Or ask the user for this too if needed

    # Read the content from the input file
    content = read_file(input_file)

    if content is not None:
        # Modify the content
        modified_content = modify_content(content)

        # Write the modified content to the output file
        write_file(output_file, modified_content)
    else :
        print("No content to write to the output file.")
        
if __name__ == "__main__":
    main()
# Question 2
# Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
def get_filename_from_user():
    """
    Prompts the user to enter a filename and ensures the file exists and can be read.
    
    :return: Valid filename entered by the user.
    """
    while True:
        filename = input("Please enter the filename: ")
        try:
            with open(filename, 'r') as file:
                # Test if the file can be opened and read
                file.read()
            return filename
        except FileNotFoundError:
            print(f"Error: The file '{filename}' does not exist. Please try again.")
        except PermissionError:
            print(f"Error: You do not have permission to read the file '{filename}'. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")
            
if __name__ == "__main__":
        # Call the get_filename_from_user function directly
        filename = get_filename_from_user()
        print(f"Valid filename entered: {filename}")


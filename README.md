# File Handler Script

## Overview

This Python script reads a specified input file, modifies its content, and writes the modified version to a new output file. It also includes functionality to prompt the user for a filename, ensuring that the file exists and can be read.

## Features

- **Read File Content:** The script reads content from a user-specified file.
- **Modify Content:** The content is converted to uppercase and appended with a custom message.
- **Write to Output File:** The modified content is written to a new file named `output.txt`.
- **Error Handling:** The script checks for errors such as file not found or permission issues when accessing the file.

## Requirements

- Python 3.x
- No external libraries are required.

## Usage

1. **Clone the Repository or Download the Script:**
   Download the script to your local machine.

2. **Run the Script:**
   Open a terminal or command prompt and navigate to the directory where the script is located. Run the following command:
   python3 file_handler.py or python3 file_program.py

3. **Input Filename:**
When prompted, enter the name of the input file (e.g., input.txt). Ensure the file is located in the same directory as the script or provide the full path.

4. **Check Output:**
After execution, a new file named output.txt will be created in the same directory, containing the modified content.

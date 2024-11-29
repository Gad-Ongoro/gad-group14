"""
- File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
- Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
"""


def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, "r") as input_file:
            content = input_file.read()

        # content modification
        modified_content = content.upper()

        # modified content to output file
        with open(output_filename, "w") as output_file:
            output_file.write(modified_content)

        print(f"Content has been successfully written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: There was an issue with reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# user input
def get_filename_from_user():
    input_filename = input("Enter the name of the file to read: ")
    output_filename = input("Enter the name of the new file to write: ")

    read_and_modify_file(input_filename, output_filename)

# run the program
get_filename_from_user()

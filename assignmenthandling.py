# file_handling_assignment.py

def create_and_write_file():
    try:
        # Create a new file and write initial content
        with open('my_file.txt', 'w') as file:
            file.write("Hello, this is the first line.\n")
            file.write("This is the second line with a number: 12345.\n")
            file.write("And this is the third line, nice to meet you!\n")
        print("File created and initial content written successfully.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def read_and_display_file():
    try:
        # Read the content of the file
        with open('my_file.txt', 'r') as file:
            content = file.read()
        print("File content read successfully. The content is:")
        print(content)
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("Permission denied to read the file.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def append_to_file():
    try:
        # Open the file in append mode and add additional content
        with open('my_file.txt', 'a') as file:
            file.write("Appending this fourth line.\n")
            file.write("Here is the fifth line with another number: 67890.\n")
            file.write("Finally, this is the sixth line, appended successfully!\n")
        print("Additional content appended successfully.")
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("Permission denied to append to the file.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def main():
    create_and_write_file()
    read_and_display_file()
    append_to_file()
    read_and_display_file()  # Read again to show appended content

if __name__ == "__main__":
    main()

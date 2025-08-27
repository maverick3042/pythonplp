def modify_content(content):
    """
    Function to modify file content.
    For this example, we'll convert text to uppercase.
    You can customize this logic.
    """
    return content.upper()

try:
    # Ask the user for the input file name
    input_file = input("Enter the name of the file to read: ")

    # Attempting to open and read the file
    with open(input_file, 'r') as file:
        content = file.read()
    
    # Modify the content
    modified_content = modify_content(content)

    # Create a new file for writing modified content
    output_file = "modified_" + input_file
    with open(output_file, 'w') as file:
        file.write(modified_content)
    
    print(f"✅ Modified content written to '{output_file}' successfully!")

except FileNotFoundError:
    print("❌ Error: The file does not exist. Please check the filename and try again.")

except PermissionError:
    print("❌ Error: You do not have permission to read this file.")

except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")

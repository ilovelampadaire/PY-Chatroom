"""
    Module that, upon imported, gets the handling text file from raw
    and writes its base64 equivalent.
"""
import base64

# Define the path to the handling.txt file
FILE_PATH = '../handling.txt'  # Adjust the path as necessary

# Read the content of the file
with open(FILE_PATH, 'r', encoding="utf8") as file:
    file_content = file.read()

    # Encode the content in Base64
    encoded_content = base64.b64encode(file_content.encode('utf-8')).decode('utf-8')

    # Write the encoded content back to the file
    try:
        with open(FILE_PATH, 'w', encoding="utf8") as file:
            file.write(encoded_content)
        print(f"File '{FILE_PATH}' has been encoded in Base64.")
    except FileNotFoundError:
        print("File not found (Handling.txt). Please recover the file.")

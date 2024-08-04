import base64

# Define the path to the handling.txt file
file_path = '../handling.txt'  # Adjust the path as necessary

# Read the content of the file
with open(file_path, 'r') as file:
    file_content = file.read()

# Encode the content in Base64
encoded_content = base64.b64encode(file_content.encode('utf-8')).decode('utf-8')

# Write the encoded content back to the file
with open(file_path, 'w') as file:
    file.write(encoded_content)

    if FileNotFoundError:
        print("File not found (Handling.txt). Please recover the file.")


print(f"File '{file_path}' has been encoded in Base64.")

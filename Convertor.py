import base64

# This function encodes file into string
# Example: file_str = encode_file_to_str("image.png")

def encode_file_to_str(file_path):    # Input: path of the file which needs to be converted
    file = open(file_path, "rb")
    file_base64 = base64.b64encode(file.read())
    file_str = file_base64.decode('utf-8')
    file.close()

    return file_str    # Output: string version of the file

# This function decodes string to file
# Example: decode_str_to_file(file_str, "image.png")

def decode_str_to_file(file_str, file_path):    # Input: string version of the file
    file = open(file_path, 'wb')
    file_byte = str.encode(file_str)
    file_base64 = base64.b64decode(file_byte)
    file.write(file_base64)
    file.close()

    return file_path    # Output: path of the file at which file has been saved
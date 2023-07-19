def encoder(string):
    encoded_string = []

    for ii in string:
        encoded_char = str((int(ii) + 3) % 10)
        encoded_string += encoded_char

    return encoded_string
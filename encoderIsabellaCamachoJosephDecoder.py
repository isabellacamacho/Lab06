# Lab 06 Isabella Camacho Encoder / Decoder

# Encoder
def encoder(password):
    encoded_pass = []
    for i in range(len(password)):
        # iterations is the length of the password
        current = int(password[i])
        # current position
        new = str(current + 3)
        # updated position adding 3 encode
        encoded_pass.append(new)
        # adding it to the encoded variable
    return "".join(encoded_pass)
    # eliminating the spaces to make it a string


def decoder(string):
    decoded_string = []

    for ii in string:
        decoded_char = str((int(ii) - 3) % 10)
        decoded_string += decoded_char
    decoded_string = ''.join(decoded_string)
    return decoded_string


def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = input("Please enter an option: ")
        if option == "1":
            password = input("Please enter password to encode: ")
            encoded_pass = encoder(password)
            print("Your password has been encoded and stored!\n")

        elif option == "2":
            print(f"The encoded password is {encoded_pass}, and the original password is {decoder(encoded_pass)}.\n")

        else:
            break


if __name__ == '__main__':
    main()


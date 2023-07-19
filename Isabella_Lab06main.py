#Isabella Camacho main Lab 06


program = True
while program:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    option = input("Please enter an option: ")
    if option == "1":
        password = input("Please enter password to encode: ")
        encoded_pass = encoder(password)
        print("Your password has been encoded and stored!\n")

    elif option == "2":
        pass

    else:
        program = False
        break

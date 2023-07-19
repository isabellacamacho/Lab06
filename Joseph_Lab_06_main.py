def main():
    while True:
        menu = int(input("\nPress 1 to encode or Press 2 to decode or Press 3 to quit: "))

        if menu == 1:
            string = input("Enter 8 integer string to encode: ")
            result = ''.join(encoder(string))
            print(result)

        if menu == 2:
            pass

        if menu == 3:
            break


if __name__ == '__main__':
    main()

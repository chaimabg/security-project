from Menu import Menu

menu = Menu()


def main():

    print("  ╔═╗ ╔═ ╔═ ╔ ╗ ╔═╗ ═╦═ ═╦═ ╔ ╗")
    print("  ╚═╗ ║═ ║  ║ ║ ║═╣  ║   ║  ║═╝" )
    print("  ╚═╝ ╚═ ╚═ ╚═╝ ╩ ╩ ═╩═  ╩  ╚═╝ ")
    print("   ╔═╗ ╔═╗ ╔═╗  ═╦═ ╔═ ╔═ ═╦═")
    print("   ║═╝ ║═╣ ║ ║ ╔ ║  ║═ ║   ║")
    print("   ╩   ╩ ╩ ╚═╝ ╚═╝  ╚═ ╚═  ╩")
    print("-------------------------------")
    print("---- Welcome To our Menu -----")
    print("-------------------------------")
    print("   Realized by :")
    print("        ↪ Abidi Amal ")
    print("        ↪ Ben Ghanem Chaima  ")
    print("-------------------------------")

    while True:
        print("       ✹✹✹ Menu ✹✹✹")
        print("1. Encoding & Decoding a message")
        print("2. Hashing a message")
        print("3. Cracking a hashed message")
        print("4. Encrypting & Decrypting a message (Symmetric)")
        print("5. Encrypting & Decrypting a message (Asymmetric)")
        print("6. ChatRoom")
        print("7. Exit")
        print("         ✹✹✹✹")
        number = input("Choose a number : ")
        if number == "1":
            print(" ")
            print("   a- Encoding")
            print("   b- Decoding")
            print(" ")
            letter = input("Choose a letter :")
            if letter == "a":
                menu.encodage()
            elif letter == "b":
                menu.decodage()
            else:
                print("Try again !")
        elif number == "2":
            print(" ")
            print("   a- MD5")
            print("   b- SHA1")
            print("   c- SHA256")
            print(" ")
            letter = input("Choose a letter :")
            if letter == "a":
                menu.hachageMD5()
            elif letter == "b":
                menu.hachageSHA1()
            elif letter == "c":
                menu.hachageSHA256()
            else:
                print("Try again !")
        elif number == "3":
            print(" ")
            print("   a- MD5")
            print("   b- SHA1")
            print("   c- SHA256")
            print(" ")
            letter = input("Choose a letter :")
            if letter == "a":
                menu.craquageMD5()
            elif letter == "b":
                menu.craquageSHA1()
            elif letter == "c":
                menu.craquageSHA256()
            else:
                print("Try again !")
        elif number == "4":
            print(" ")
            print("   a- DES")
            print("   b- AES256")
            print(" ")
            letter = input("Choose a letter :")
            if letter == "b":
                menu.chiffrementAES()
                print(" ")
                menu.dechiffrementAES()

            elif letter == "a":
                menu.chiffrementDES()
                print(" ")
                menu.dechiffrementDES()
            else:
                print("Try again !")
        elif number == "5":
            print(" ")
            print("   a- RSA")
            print("   b- ElGamal")
            print(" ")
            letter = input("Choose a letter :")
            if letter == "a":
                menu.chiffrementRSA()
                print(" ")
                menu.dechiffrementRSA()
            elif letter == "b":
                menu.chiffrementElGamal()
                print(" ")
                menu.dechiffrementElGamal()
            else:
                print("Try again !")
        elif number == "6":
            print('ChatRoom')
        elif number == "7":
            print("     ✹✹✹ Goodbye ✹✹✹")
            break


main()

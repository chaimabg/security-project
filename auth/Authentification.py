import hashlib
import re
import getpass
from UserService import UserService
from User import User

# regular expression for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

userService = UserService()


class Authentification(object):

    def check(self, email):
        if (re.fullmatch(regex, email)):
            return True
        else:
            print('Email invalid !')
            return False

    def register(self):
        username = input("Enter your username >> ")
        emailVerif = False

        while (not emailVerif):
            email = input("Enter your email >> ")
            if self.check(email):
                break

        password = getpass.getpass("Enter your password >> ")
        passwordVerif = getpass.getpass("Confirm your password >> ")

        while passwordVerif != password:
            passwordVerif = getpass.getpass("Confirm your password >> ")

        pwd = hashlib.sha256(password.encode()).hexdigest()
        user = User(username, email, pwd)
        userService.addUser(user)
        print(" ")
        print("    ✔  You have successfully registered !!")
        print(" ")


    def signIn(self):
        email = input("Enter your email >> ")
        password = getpass.getpass("Enter your password >> ")
        user = userService.findUser(email)
        if user is not None:
            pwd = user[2]
            pwdHashed = hashlib.sha256(password.encode()).hexdigest()
            if pwdHashed == pwd:
                code = userService.send_mail(email, user[0])
                print("Check your email !")
                validationCode = input("Enter the validation code >> ")
                if str(code) != validationCode:
                    print("TRY AGAIN !")
                    self.signIn()
                print(" ")
                print("    ✔  Welcome", user[0], "🙈")
                print(" ")
            else:
                print("😒  Password or Email Incorrect  😒")
                self.signIn()
        else:
            print("😒  Password or Email Incorrect  😒")
            self.signIn()





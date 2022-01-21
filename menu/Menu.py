import hashlib
import rsa

from elgamal import elgamal
from des import DesKey
from Cryptodome.Cipher import AES
from Cryptodome import Random
from Cryptodome.Random import get_random_bytes

BLOCK_SIZE = 16

key0 = DesKey(b"some key")

pubkeyRSA, privkeyRSA = rsa.newkeys(512)

keys = elgamal.generate_keys()
pubKeyElGamal = keys['publicKey']
privKeyElGamal = keys['privateKey']

keyAES = get_random_bytes(16)
IV = Random.new().read(BLOCK_SIZE)
dictionnaire_path="dictionnaire.txt"

class Menu():

    # -------- Codage & Decodage --------
    def encodage(self):
        msg = input("Enter the message to encode : \n")
        msgEncode = msg.encode("utf-8")
        print('The message is : ', msg)
        print('The message encoded : ', msgEncode.hex())

    def decodage(self):
        msg = input("Enter the message to decode : \n")
        msgdec = bytes.fromhex(msg).decode("utf-8")
        print('The message decoded : ', msgdec)

    # -------- Hachage --------
    def hachageMD5(self):
        msg = input("Enter the message to hash : \n")
        msgEncode = msg.encode("utf-8")
        result = hashlib.md5(msgEncode).hexdigest()
        print('The message is : ', msg)
        print('The message hashed with MD5 : ', result)

    def hachageSHA1(self):
        msg = input("Enter the message to hash : \n")
        msgEncode = msg.encode("utf-8")
        result = hashlib.sha1(msgEncode).hexdigest()
        print('The message is : ', msg)
        print('The message hashed with SHA1 : ', result)

    def hachageSHA256(self):
        msg = input("Enter the message to hash : \n")
        msgEncode = msg.encode("utf-8")
        result = hashlib.sha256(msgEncode).hexdigest()
        print('The message is : ', msg)
        print('The message hashed with SHA1 : ', result)

    # -------- Craquage --------
    def craquageMD5(self):
        msg = input("Enter the message to crack : \n")
        try:
            fp = open(dictionnaire_path)
            line = fp.readline().strip()
            while line:
                msgEncode = line.encode("utf-8")
                result = hashlib.md5(msgEncode).hexdigest()
                if result == msg:
                   print("The message cracked : ", line)
                   break
                line = fp.readline().strip()
            print('✦✦✦ Cracking ended ✦✦✦')
        finally:
            fp.close()

    def craquageSHA1(self):
        msg = input("Enter the message to crack : \n")
        try:
            fp = open(dictionnaire_path)
            line = fp.readline().strip()
            while line:
                msgEncode = line.encode("utf-8")
                result = hashlib.sha1(msgEncode).hexdigest()
                if result == msg:
                    print("The message cracked : ", line)
                    break
                line = fp.readline().strip()
            print('✦✦✦ Cracking ended ✦✦✦')
        finally:
            fp.close()

    def craquageSHA256(self):
        msg = input("Enter the hashed message to crack : \n")
        try:
            fp = open(dictionnaire_path)
            line = fp.readline().strip()
            while line:
                msgEncode = line.encode("utf-8")
                result = hashlib.sha256(msgEncode).hexdigest()
                if result == msg:
                    print("The message cracked : ", line)
                    break
                line = fp.readline().strip()
            print('✦✦✦ Cracking ended ✦✦✦')
        finally:
            fp.close()

    # -------- Chiffrement Symetrique --------
    def chiffrementDES(self):
        msg = input("Enter the message to encrypt : \n")
        enctex = key0.encrypt(msg.encode("utf-8"), padding=True)
        print('The message sent is : ', msg)
        print('The message encrypted with DES:\n ', enctex.hex())

    def dechiffrementDES(self):
        msg = input("Enter the message to decrypt : \n")
        dectex = key0.decrypt(bytes.fromhex(msg), padding=True).decode()
        print('The message decrypted with DES:\n ', dectex)

    def chiffrementAES(self):
        msg = input("Enter the message to encrypt : \n")
        aes = AES.new(keyAES, AES.MODE_CFB, IV)
        enctex= aes.encrypt(msg.encode())
        print('The message sent is : ', msg)
        print('The message encrypted with AES256:\n ',enctex.hex())

    def dechiffrementAES(self):
        msg = input("Enter the message to decrypt : \n")
        aes = AES.new(keyAES, AES.MODE_CFB, IV)
        dectex= aes.decrypt(bytes.fromhex(msg)).decode()
        print('The message decrypted with AES256:\n ',dectex)

    # -------- Chiffrement Asymetrique --------
    def chiffrementRSA(self):
        msg = input("Enter the message to encrypt : \n")
        enctex = rsa.encrypt(msg.encode(), pubkeyRSA)
        print('The message sent is : ', msg)
        print('The message encrypted with RSA:\n ', enctex.hex())

    def dechiffrementRSA(self):
        msg = input("Enter the message to decrypt : \n")
        dectex = rsa.decrypt(bytes.fromhex(msg), privkeyRSA).decode()
        print('The message decrypted with RSA : ', dectex)

    def chiffrementElGamal(self):
        msg = input("Enter the message to encrypt : \n")
        enctex = elgamal.encrypt(pubKeyElGamal, msg)
        print('The message sent is : ', msg)
        print('The message encrypted with ElGamal:\n ', enctex)

    def dechiffrementElGamal(self):
        msg = input("Enter the message to decrypt : \n")
        dd = elgamal.decrypt(privKeyElGamal, msg)
        print('The message decrypted with ElGamal : ', dd)


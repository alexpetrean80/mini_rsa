# from lib.encryption import encrypt, EncryptionData
from lib.utils.alphabet import Alphabet
from lib.decryption import PrivateKeyOwner
from lib.encryption import PublicKeyOwner
from lib.key_generation import generating_primes
if __name__ == '__main__':

    p, q = generating_primes(1024)
    a = Alphabet(" ABCDEFGHIJKLMNOPQRSTUVWXYZ012345689")

    pv = PrivateKeyOwner(a, p, q)
    pb = PublicKeyOwner(pv)

    text = "CRYPTOGRAPHY 10 YAY"

    cipher_text = pb.encrypt(text)

    print(cipher_text)

    plain_text = pv.decrypt(cipher_text)

    print(plain_text)

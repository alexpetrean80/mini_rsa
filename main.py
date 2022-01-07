# from lib.encryption import encrypt, EncryptionData
from lib.utils.alphabet import Alphabet
from lib.decryption import PrivateKeyOwner
from lib.encryption import PublicKeyOwner

if __name__ == '__main__':
    a = Alphabet(" ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    p = 31
    q = 43

    pv = PrivateKeyOwner(a, p, q)
    pb = PublicKeyOwner(pv)

    text = "CRYPTO"

    cipher_text = pb.encrypt(text)

    print(cipher_text)

    plain_text = pv.decrypt(cipher_text)

    print(plain_text)

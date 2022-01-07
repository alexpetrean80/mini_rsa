from math import gcd
from dataclasses import dataclass
from functools import reduce

from lib.decryption import PrivateKeyOwner
from lib.utils.alphabet import Alphabet
from lib.utils.strings import split_into_blocks


@dataclass
class PublicKeyOwner:
    alphabet: Alphabet
    n: int
    e: int
    plain_block_size: int  # k
    cipher_block_size: int  # l

    def __init__(self, pk_owner: PrivateKeyOwner):
        self.alphabet = pk_owner.alphabet
        self.n = pk_owner.n
        self.e = pk_owner.e
        self.plain_block_size = pk_owner.plain_block_size
        self.cipher_block_size = pk_owner.cipher_block_size

    def __get_blocks(self, text):
        return split_into_blocks(text, self.plain_block_size)

    def __encrypt_blocks(self, bs):
        return [pow(b, self.e, self.n) for b in bs]

    def encrypt(self, text) -> str:
        bs = [self.alphabet.text_to_base10(b) for b in self.__get_blocks(text)]
        c_bs = [self.alphabet.base10_to_text(b) for b in self.__encrypt_blocks(bs)]

        for i in range(len(c_bs)):

            block_len = len(c_bs[i])
            if block_len < self.cipher_block_size:
                c_bs[i] = (" " * (self.cipher_block_size - block_len)) + c_bs[i]

        return reduce(lambda cipher_text, block: cipher_text + block, c_bs)

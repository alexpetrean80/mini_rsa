from dataclasses import dataclass
from math import gcd
from functools import reduce

from lib.utils.alphabet import Alphabet
from lib.utils.strings import split_into_blocks


@dataclass
class PrivateKeyOwner:
    alphabet: Alphabet
    n: int
    e: int
    __d: int
    plain_block_size: int  # k
    cipher_block_size: int  # l

    def __init__(self, alphabet, p, q):
        self.alphabet = alphabet
        self.n = p * q
        euler = (p - 1) * (q - 1)
        self.e = self.__generate_public_key(euler)
        self.__d = self.__generate_private_key(euler)
        self.__establish_block_sizes()  # check course 5 slide 22 for explanation

    def __generate_public_key(self, euler):

        for e in range(3, euler, 2):
            if gcd(e, euler) == 1:
                return e
        return -1

    def __generate_private_key(self, euler):
        return pow(self.e, -1, euler)

    def __establish_block_sizes(self):  # course 5 slide 22 explains block sizes for enc and dec and their properties
        self.plain_block_size = 1
        self.cipher_block_size = 1

        x = self.alphabet.get_size()

        while x < self.n:
            self.plain_block_size = self.cipher_block_size
            self.cipher_block_size += 1
            x *= self.alphabet.get_size()

    def get_public_key(self) -> (int, int):  # ( n, e)
        return self.n, self.e

    def __decrypt_blocks(self, blocks):
        blocks_as_numbers = [self.alphabet.text_to_base10(block) for block in blocks]

        decrypted_blocks = [pow(number, self.__d, self.n) for number in blocks_as_numbers]

        return [self.alphabet.base10_to_text(block) for block in decrypted_blocks]

    def decrypt(self, text: str) -> str:
        blocks = split_into_blocks(text, self.cipher_block_size)
        decrypted_blocks = self.__decrypt_blocks(blocks)
        return reduce(lambda plain_text, block: plain_text + block, decrypted_blocks)

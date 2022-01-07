import copy
from dataclasses import dataclass
from functools import reduce


@dataclass
class Alphabet:
    __alphabet: str

    __size: int

    def __init__(self, alphabet):
        self.__alphabet = copy.copy(alphabet)
        self.__size = len(self.__alphabet)

    def get_size(self):
        return self.__size

    def char_to_base10(self, char: str) -> int:
        if len(char) != 1:
            return -1

        for i, v in enumerate(self.__alphabet):
            if v == char:
                return i
        return -1

    def text_to_base10(self, text: str) -> int:

        text_len = len(text)
        val = 0
        index_power = pow(self.__size, text_len - 1)

        for i, char in enumerate(text):
            char_value = self.char_to_base10(char)

            val += char_value * index_power
            index_power //= self.__size

        return val

    def base10_to_text(self, val: int) -> str:

        if 0 <= val < self.__size:
            return self.__alphabet[val]

        rests = []
        while val != 0:
            rests.append(int(val % self.__size))
            val //= self.__size

        rests.reverse()

        return reduce(lambda text, rest: text + self.__alphabet[rest], rests, "")

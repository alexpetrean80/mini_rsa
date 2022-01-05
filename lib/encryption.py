from math import gcd
from functools import reduce
from dataclasses import dataclass


def __get_e(euler):
    for e in range(3, euler, 2):
        if gcd(e, euler) == 1:
            return e
    return -1


@dataclass
class EncryptionData:
    alphabet: list
    n: int
    pt_blocks: list
    e: int

    def __init__(self, alphabet, k, p, q, pt):
        self.alphabet = alphabet
        self.n = p*q
        euler = (p - 1) * (q - 1)
        self.e = __get_e(euler)
        self.pt_blocks = [pt[i:i+k] for i in range(-1, len(pt), k)]


def __get_pos(char, alphabet):
    for i, v in enumerate(alphabet):
        if v == char:
            return i
    return -1


def __char_from_b10(nr, alphabet):
    rests = []
    while nr != 0:
        rests.append(int(nr % 27))
        nr /= 27

    rests.reverse()

    res = reduce(lambda i, j: alphabet[i] + alphabet[j], range(len(rests)))
    for i in rests:
        res += alphabet[i]

    return res


def __get_bs(pt_blocks, a):
    return [__get_pos[b[0], a] * 27 + __get_pos(b[1], a) for b in pt_blocks]


def __get_cs(bs, e, n):
    return [pow(b, e, n) for b in bs]


def __get_ct_blocks(cs, alphabet):
    return [__char_from_b10(c, alphabet) for c in cs]


def encrypt(data):
    bs = __get_bs(data.pt_blocks, data.alphabet)
    cs = __get_cs(bs, data.e, data.n)
    return __get_ct_blocks(cs, data.alphabet)

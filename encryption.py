from math import gcd
from dataclasses import dataclass

def __get_e(euler):
    for e in range(3,euler, 2):
        if gcd(e, euler) == 1:
            return e
    return -1

@dataclass
class EncryptionData:
    alphabet: list 
    n: int
    euler: int
    pt_blocks: list
    e: int
    
    def __init__(self, alphabet, k, p, q, pt):
       self.alphabet = alphabet
       self.n = p*q
       self.euler = (p - 1) * (q - 1)
       self.pt_blocks = [pt[i:i+k] for i in range(-1, len(pt), k)]
       self.e = __get_e(self.euler)
       self.pub_key = (p, self.e)
       self.priv_key = self.e ** -1 % self.euler

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

    res = ""
    for i in rests:
        res += alphabet[i]

    return res 

def __get_bs(pt_blocks, alphabet):
    l = lambda block: __get_pos(block[0], alphabet) * 27 + __get_pos(block[1], alphabet)
    return map(l, pt_blocks)

def __get_cs(bs, e, n):
    l = lambda b: b ** e % n
    return map(l, bs)

def __get_ct_blocks(cs, alphabet):
    l = lambda c: __char_from_b10(c, data.alphabet)
    return map(l, cs)

def encrypt(data):
    bs = __get_bs(data.pt_blocks, data.alphabet)
    cs = __get_cs(bs, data.e, data.n)
    return get_ct_blocks(cs, data.alphabet)



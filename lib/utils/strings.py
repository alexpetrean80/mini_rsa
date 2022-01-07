def split_into_blocks(s: str, b_size: int) -> [str]:
    while len(s) % b_size != 0:  # pad with space at the end until the string can be split into blocks of size b_size
        s += " "

    b_count = len(s) // b_size
    blocks = []

    for i in range(b_count):
        blocks.append(s[i * b_size:(i + 1) * b_size])

    return blocks

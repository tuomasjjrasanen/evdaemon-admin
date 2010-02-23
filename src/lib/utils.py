def hexstrs_to_int(hexstrs):
    hexsumstr = ''
    hexvals = [int(v, 16) for v in hexstrs]
    for hexval in hexvals:
        padded_hexval = format(hexval, "016x")
        assert(len(padded_hexval) == 16)
        hexsumstr += padded_hexval
    return int(hexsumstr, 16)

def hexline_to_int(hexline):
    return hexstrs_to_int(hexline.split())

def int_to_hexline(value):
    hexstr = format(value, "x")
    blocks = []
    block = []
    for char in reversed(hexstr):
        block.append(char)
        if len(block) == 16:
            if all([c == block[0] for c in block[1:]]):
                blocks.append("0")
            else:
                # format(int()) to remove leading zeros, hacky but works.
                blocks.append(format(int("".join(reversed(block)), 16), "x"))
            block = []
    if block:
        blocks.append("".join(reversed(block)))
    return " ".join(reversed(blocks))

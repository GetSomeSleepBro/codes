#!/usr/bin/env python3
"""
Error Detection & Correction for 7/8-bit ASCII codes using the (12,8) Hamming code.

The (12,8) Hamming code adds four parity bits (at indices that are a power of two)
to every 8 data bits. It can correct all single-bit errors and detect all double-bit
errors within the 12-bit code-word.

Usage examples
--------------
Encode a string:
    $ python hamming_error_detection.py encode "HELLO"

Introduce an error in a single bit position (0-based) and decode:
    $ python hamming_error_detection.py decode 010011001010,5

Where the comma separates the code-word and the index at which the bit is flipped.

You can also decode without errors:
    $ python hamming_error_detection.py decode 010011001010
"""

import sys
from typing import Tuple, List


PARITY_POSITIONS = (0, 1, 3, 7)  # zero-based positions within a 12-bit word


def _calculate_parity_bits(codeword: List[int]) -> List[int]:
    """Return the four parity bits for a 12-bit codeword (with zeros in parity positions)."""
    parity = []
    for p in PARITY_POSITIONS:
        index = p + 1  # convert to 1-based for math convenience
        xor_sum = 0
        for i in range(1, 13):
            if i & index and i != index:  # skip the parity bit itself
                xor_sum ^= codeword[i - 1]
        parity.append(xor_sum)
    return parity


def _place_data_bits(data_bits: List[int]) -> List[int]:
    """Return a 12-bit list with data bits placed; parity positions filled with 0."""
    codeword = [0] * 12
    j = 0
    for i in range(12):
        if i not in PARITY_POSITIONS:
            codeword[i] = data_bits[j]
            j += 1
    return codeword


def encode_char(char: str) -> str:
    """Encode a single character into its 12-bit Hamming representation."""
    ascii_val = ord(char)
    data_bits = [(ascii_val >> (7 - i)) & 1 for i in range(8)]  # 8 bits
    codeword = _place_data_bits(data_bits)

    parity_bits = _calculate_parity_bits(codeword)
    for idx, p in zip(PARITY_POSITIONS, parity_bits):
        codeword[idx] = p
    return ''.join(str(b) for b in codeword)


def encode(message: str) -> str:
    """Return a concatenated string of 12-bit codewords representing *message*."""
    return ' '.join(encode_char(c) for c in message)


def _syndrome(received: List[int]) -> int:
    """Compute the error syndrome for a 12-bit received codeword."""
    parity = _calculate_parity_bits(received)
    syndrome = 0
    for bit, position in zip(parity, PARITY_POSITIONS):
        if bit != received[position]:
            syndrome += position + 1  # convert to 1-based
    return syndrome


def decode_codeword(bits: str) -> Tuple[str, bool]:
    """Decode a 12-bit *bits* string.

    Returns (decoded_character, error_corrected_flag)
    """
    if len(bits) != 12 or any(b not in '01' for b in bits):
        raise ValueError("Codeword must be a 12-bit binary string.")
    received = [int(b) for b in bits]
    syndrome = _syndrome(received)
    corrected = False
    if syndrome != 0 and syndrome <= 12:
        # Correct single-bit error
        corrected = True
        received[syndrome - 1] ^= 1

    # Extract data bits (positions that are not parity bits)
    data_bits = [received[i] for i in range(12) if i not in PARITY_POSITIONS]
    ascii_val = 0
    for bit in data_bits:
        ascii_val = (ascii_val << 1) | bit
    return chr(ascii_val), corrected


def decode(ciphertext: str) -> str:
    """Decode a sequence of space-separated 12-bit codewords."""
    parts = ciphertext.strip().split()
    decoded_chars = []
    for cw in parts:
        ch, _ = decode_codeword(cw)
        decoded_chars.append(ch)
    return ''.join(decoded_chars)


def _flip_bit(word: str, index: int) -> str:
    if not 0 <= index < len(word):
        raise ValueError("Index out of bounds.")
    flipped = list(word)
    flipped[index] = '1' if word[index] == '0' else '0'
    return ''.join(flipped)


def main(argv: List[str]):
    if len(argv) < 2 or argv[1] not in {"encode", "decode"}:
        print("Usage: {} encode <message> | decode <codeword>[,<error_index>]".format(argv[0]))
        return

    mode = argv[1]
    if mode == "encode":
        if len(argv) < 3:
            print("Provide a message to encode.")
            return
        message = ' '.join(argv[2:])
        print(encode(message))
    else:  # decode
        if len(argv) < 3:
            print("Provide a 12-bit codeword (or codewords).")
            return
        arg = argv[2]
        if ',' in arg:
            word, idx = arg.split(',', 1)
            try:
                idx = int(idx)
            except ValueError:
                print("Invalid error index.")
                return
            word = _flip_bit(word, idx)
            print("Introduced error at position {} -> {}".format(idx, word))
            print("Decoded:", decode(word))
        else:
            print(decode(arg))


if __name__ == "__main__":
    main(sys.argv)

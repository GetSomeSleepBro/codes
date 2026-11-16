import heapq
from collections import Counter


class Node:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None


def build_tree(text):
    frequencies = Counter(text)
    heap = []

    for number, (character, frequency) in enumerate(frequencies.items()):
        node = Node(character, frequency)
        heapq.heappush(heap, (frequency, number, node))

    next_number = len(heap)

    if len(heap) == 1:
        return heap[0][2], frequencies

    while len(heap) > 1:
        first_frequency, _, first_node = heapq.heappop(heap)
        second_frequency, _, second_node = heapq.heappop(heap)

        parent = Node(None, first_frequency + second_frequency)
        parent.left = first_node
        parent.right = second_node
        heapq.heappush(heap, (parent.frequency, next_number, parent))
        next_number += 1

    return heap[0][2], frequencies


def make_codes(root, code, codes):
    if root.character is not None:
        codes[root.character] = code if code else "0"
        return

    make_codes(root.left, code + "0", codes)
    make_codes(root.right, code + "1", codes)


def decode_text(encoded_text, root):
    if root.left is None and root.right is None:
        return root.character * len(encoded_text)

    decoded_characters = []
    current = root

    for bit in encoded_text:
        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.character is not None:
            decoded_characters.append(current.character)
            current = root

    return "".join(decoded_characters)


def main():
    text = input("Enter a string: ")

    if not text:
        print("String cannot be empty.")
        return

    root, frequencies = build_tree(text)
    codes = {}
    make_codes(root, "", codes)

    print("\nCharacter Frequencies:")
    for character, frequency in sorted(frequencies.items()):
        print(repr(character), ":", frequency)

    print("\nHuffman Codes:")
    for character, code in sorted(codes.items()):
        print(repr(character), ":", code)

    encoded_text = "".join(codes[character] for character in text)
    decoded_text = decode_text(encoded_text, root)

    original_bits = len(text.encode("utf-8")) * 8
    encoded_bits = len(encoded_text)

    print("\nEncoded String:", encoded_text)
    print("Decoded String:", decoded_text)
    print("Original size:", original_bits, "bits (UTF-8)")
    print("Encoded size:", encoded_bits, "bits")

    if encoded_bits > 0:
        compression_ratio = original_bits / encoded_bits
        space_saved = (1 - encoded_bits / original_bits) * 100
        print("Compression ratio:", round(compression_ratio, 2), ": 1")
        print("Space saved:", round(space_saved, 2), "%")
        

if __name__ == "__main__":
    main()


# SAMPLE OUTPUT:
# Enter a string: BANANA
#
# Character Frequencies:
# 'A' : 3
# 'B' : 1
# 'N' : 2
#
# Huffman Codes:
# 'A' : 0
# 'B' : 10
# 'N' : 11
#
# Encoded String: 100110110
# Decoded String: BANANA
# Original size: 48 bits (UTF-8)
# Encoded size: 9 bits
# Compression ratio: 5.33 : 1
# Space saved: 81.25 %

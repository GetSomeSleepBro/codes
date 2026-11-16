# ============================================================
# A(2) Write a program to implement Huffman Encoding
# using a greedy strategy.
# ============================================================

import heapq


def huffman(text):
    # Count character frequencies
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    # Create min heap
    heap = [(f, i, ch) for i, (ch, f) in enumerate(freq.items())]
    heapq.heapify(heap)
    count = len(heap)

    # Build Huffman Tree
    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)

        heapq.heappush(heap, (f1 + f2, count, (left, right)))
        count += 1

    # Generate Huffman Codes
    codes = {}

    def generate(node, code=""):
        if isinstance(node, str):
            codes[node] = code or "0"
        else:
            generate(node[0], code + "0")
            generate(node[1], code + "1")

    generate(heap[0][2])

    return codes


# Main Program
text = input("Enter text: ")

if not text:
    print("Please enter some text.")
else:
    codes = huffman(text)

    print("\nHuffman Codes:")
    for ch, code in codes.items():
        print(f"{ch} : {code}")

    encoded = "".join(codes[ch] for ch in text)

    print("\nOriginal Text:", text)
    print("Encoded Text :", encoded)
    print("Original Size:", len(text) * 8, "bits")
    print("Encoded Size :", len(encoded), "bits")


# ============================================================
# SAMPLE OUTPUT
# ============================================================
#
# Enter text: aaabbc
#
# Huffman Codes:
# a : 0
# c : 10
# b : 11
#
# Original Text: aaabbc
# Encoded Text : 000111110
# Original Size: 48 bits
# Encoded Size : 9 bits
#
# Note: Assumes 8 bits per input character.
# Encoding size excludes tree/codebook storage overhead.


# ============================================================
# ------------------------------------------------------------
# THEORY AND VIVA QUESTIONS & ANSWERS
# ------------------------------------------------------------
# ============================================================

# THEORY:
#
# Huffman Encoding is a lossless compression algorithm
# that uses a greedy strategy.
#
# Frequently occurring characters get shorter binary codes,
# while less frequent characters get longer codes.
#
# ALGORITHM:
# 1. Count frequency of each character.
# 2. Create a min heap using frequencies.
# 3. Remove two minimum-frequency nodes.
# 4. Merge them and insert back into the heap.
# 5. Repeat until only one node remains.
# 6. Assign 0 to left and 1 to right branches.
# 7. Generate binary codes for each character.
#
# COMPLEXITY:
# n = Total characters, k = Unique characters
# B = Number of encoded bits
#
# Tree Construction: O(k log k)
# Total Time       : O(n + k log k + B)
# Space            : O(k + B), including encoded output


# Q1. What is Huffman Encoding?
# Ans: A lossless compression algorithm that assigns
# variable-length binary codes based on character frequency.


# Q2. Why is it called a Greedy Algorithm?
# Ans: It repeatedly selects the two lowest-frequency
# nodes, making the locally optimal choice at each step.


# Q3. What is a Greedy Algorithm?
# Ans: An algorithm that makes the best immediate choice
# at each step to achieve an optimal solution.


# Q4. Why do we use a Min Heap?
# Ans: To efficiently find and remove the two nodes
# having the lowest frequencies.


# Q5. What is heapq?
# Ans: Python's built-in min-heap library.
# Insertion and removal take O(log k) time.


# Q6. Why do frequent characters get shorter codes?
# Ans: Because shorter codes for frequent characters
# reduce the total number of encoded bits.


# Q7. What is a Huffman Tree?
# Ans: A binary tree where leaf nodes represent characters
# and internal nodes represent combined frequencies.


# Q8. What is time complexity?
# Ans: It measures how execution time grows with input size.
# Huffman tree construction takes O(k log k) time.


# Q9. What is space complexity?
# Ans: It measures memory usage.
# The tree and codebook require O(k) space.
# Encoded output additionally requires O(B) space.


# Q10. What is Lossless Compression?
# Ans: Compression where the original data can be
# recovered exactly without losing information.


# Q11. What is a Prefix-Free Code?
# Ans: No character's code is a prefix of another
# character's code, allowing unambiguous decoding.


# Q12. Can characters have equal frequencies?
# Ans: Yes. Their codes may differ depending on the
# tree structure, but the encoding remains optimal.


# Q13. Where is Huffman Encoding used?
# Ans: In compression formats such as ZIP, JPEG and PNG.


# Q14. Is Huffman Encoding always smaller?
# Ans: No. For small inputs, storing the tree or codebook
# may use more space than the compression saves.


# Q15. Why is Huffman Encoding efficient?
# Ans: It uses a min heap to build an optimal prefix-free
# code and reduces bits for frequent characters.


# ============================================================
# CONCLUSION
# ============================================================
#
# Huffman Encoding uses a greedy strategy and min heap
# to perform lossless compression using binary codes.
# ============================================================

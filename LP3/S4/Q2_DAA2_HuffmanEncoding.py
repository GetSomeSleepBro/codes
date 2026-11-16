# ============================================================
# A(2) Write a program to implement Huffman Encoding
# using a greedy strategy.
# ============================================================

import heapq

def huffman(data):
    freq = {}

    # Count frequency
    for ch in data:
        freq[ch] = freq.get(ch, 0) + 1

    # Create min heap
    heap = [[f, i, ch] for i, (ch, f) in enumerate(freq.items())]
    heapq.heapify(heap)
    count = len(heap)

    # Build Huffman Tree
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)

        heapq.heappush(heap, [a[0] + b[0], count, [a, b]])
        count += 1

    # Generate codes
    def generate(node, code=""):
        if isinstance(node[2], str):
            print(node[2], ":", code or "0")
        else:
            generate(node[2][0], code + "0")
            generate(node[2][1], code + "1")

    generate(heap[0])


# Main Program
data = input("Enter string: ")

if data:
    print("\nHuffman Codes:")
    huffman(data)
else:
    print("Please enter some text.")


# ============================================================
# SAMPLE OUTPUT
# ============================================================
#
# Enter string: aaabbc
#
# Huffman Codes:
# a : 0
# c : 10
# b : 11


# ============================================================
# ------------------------------------------------------------
# THEORY AND VIVA QUESTIONS & ANSWERS
# ------------------------------------------------------------
# ============================================================

# THEORY:
# Huffman Encoding is a lossless compression algorithm
# based on the Greedy Strategy.
#
# Frequently occurring characters get shorter binary codes,
# while less frequent characters get longer codes.
#
# ALGORITHM:
# 1. Count frequency of each character.
# 2. Create a min heap.
# 3. Select two minimum-frequency nodes.
# 4. Merge them and insert into the heap.
# 5. Repeat until one root node remains.
# 6. Assign 0 to left and 1 to right branches.
#
# COMPLEXITY:
# n = Total characters, k = Unique characters
#
# Heap construction : O(k)
# Tree construction : O(k log k)
# Frequency counting: O(n)
# Tree storage      : O(k)
# Code generation also takes time to output the codes.


# Q1. What is Huffman Encoding?
# Ans: A lossless compression technique that assigns
# variable-length binary codes based on frequencies.


# Q2. What is a Greedy Algorithm?
# Ans: It selects the best immediate choice at each step
# to reach an optimal solution.


# Q3. Why is Huffman Encoding greedy?
# Ans: It repeatedly merges the two nodes with the
# lowest frequencies.


# Q4. What is a Min Heap?
# Ans: A data structure where the smallest element
# is always at the root.


# Q5. Why do we use heapq?
# Ans: It efficiently finds and removes minimum elements.
# Insertion and removal take O(log k) time.


# Q6. What is a Huffman Tree?
# Ans: A binary tree where leaf nodes represent characters
# and internal nodes store combined frequencies.


# Q7. What is time complexity?
# Ans: It describes how running time grows with input size.
# Huffman tree construction takes O(k log k).


# Q8. Why is tree construction O(k log k)?
# Ans: We perform O(k) heap operations, and each
# operation takes O(log k) time.


# Q9. What is space complexity?
# Ans: It measures memory usage.
# Huffman tree and heap require O(k) space.


# Q10. What is lossless compression?
# Ans: Compression where the original data can be
# recovered without losing information.


# Q11. Why do frequent characters get shorter codes?
# Ans: To reduce the total number of bits required
# to represent the data.


# Q12. What is a prefix-free code?
# Ans: No character's code is the prefix of another
# character's code, allowing unambiguous decoding.


# Q13. Can two characters have equal frequencies?
# Ans: Yes. Different valid Huffman codes may be produced,
# but the total encoded length remains optimal.


# Q14. Where is Huffman Encoding used?
# Ans: In compression formats such as ZIP, JPEG and PNG.


# Q15. Why is iterative Fibonacci different from Huffman?
# Ans: Fibonacci calculates a numerical sequence,
# while Huffman uses greedy tree construction for compression.


# ============================================================
# CONCLUSION
# ============================================================
#
# Huffman Encoding uses a greedy strategy and a min heap
# to generate optimal prefix-free binary codes.
# ============================================================

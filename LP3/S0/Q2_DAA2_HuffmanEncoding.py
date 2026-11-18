import heapq
from collections import Counter

text = input("Enter a string: ")

if not text:
    print("Please enter a string.")
else:
    freq = Counter(text)
    heap = [[freq[ch], [ch, ""]] for ch in freq]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        for item in left[1:]:
            item[1] = "0" + item[1]

        for item in right[1:]:
            item[1] = "1" + item[1]

        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])

    if len(freq) == 1:
        heap[0][1][1] = "0"

    print("Huffman Codes:")
    for ch, code in sorted(heap[0][1:]):
        print(ch, ":", code)

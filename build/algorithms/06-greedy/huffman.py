"""
Huffman Coding

Huffman coding is a lossless data compression algorithm that assigns variable-length
codes to characters based on their frequencies.

KEY IDEA:
    More frequent characters get shorter codes.
    Less frequent characters get longer codes.
    This minimizes total encoded length.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

import heapq
from typing import Dict, Tuple, Optional
from collections import Counter


class HuffmanNode:
    """Node for Huffman tree."""

    def __init__(self, char: Optional[str], freq: int):
        self.char = char
        self.freq = freq
        self.left: Optional['HuffmanNode'] = None
        self.right: Optional['HuffmanNode'] = None

    def __lt__(self, other: 'HuffmanNode') -> bool:
        return self.freq < other.freq


def build_huffman_tree(freq: Dict[str, int]) -> Optional[HuffmanNode]:
    """
    Build Huffman tree from character frequencies.

    ALGORITHM:
    1. Create leaf node for each character
    2. Build min-heap of all nodes
    3. While heap has more than one node:
       - Extract two minimum nodes
       - Create new internal node with sum of frequencies
       - Add new node back to heap
    4. Return root of tree
    """
    if not freq:
        return None

    if len(freq) == 1:
        char, f = list(freq.items())[0]
        root = HuffmanNode(None, f)
        root.left = HuffmanNode(char, f)
        return root

    heap = [HuffmanNode(char, f) for char, f in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(root: Optional[HuffmanNode], code: str = "",
                   codes: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    """
    Generate Huffman codes by traversing tree.

    Left edge = '0', Right edge = '1'
    """
    if codes is None:
        codes = {}

    if root is None:
        return codes

    if root.char is not None:
        codes[root.char] = code if code else "0"
        return codes

    generate_codes(root.left, code + "0", codes)
    generate_codes(root.right, code + "1", codes)

    return codes


def huffman_encode(text: str) -> Tuple[str, Dict[str, str]]:
    """
    Encode text using Huffman coding.

    Returns:
        Tuple of (encoded_string, codes_dict)
    """
    if not text:
        return "", {}

    freq = Counter(text)
    root = build_huffman_tree(freq)
    codes = generate_codes(root)

    encoded = "".join(codes[char] for char in text)
    return encoded, codes


def huffman_decode(encoded: str, codes: Dict[str, str]) -> str:
    """
    Decode Huffman-encoded string.

    ALGORITHM:
    1. Build reverse mapping (code -> char)
    2. Match bits to codes while traversing
    """
    if not encoded or not codes:
        return ""

    reverse_codes = {code: char for char, code in codes.items()}

    result = []
    current_code = ""

    for bit in encoded:
        current_code += bit
        if current_code in reverse_codes:
            result.append(reverse_codes[current_code])
            current_code = ""

    return "".join(result)


def calculate_compression_ratio(original: str, encoded: str) -> float:
    """Calculate compression ratio."""
    original_bits = len(original) * 8
    encoded_bits = len(encoded)

    if original_bits == 0:
        return 0.0

    return (1 - encoded_bits / original_bits) * 100


# =============================================================================
# TEST EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("HUFFMAN CODING DEMONSTRATION")
    print("=" * 60)

    # Basic example
    print("\n1. Basic Encoding")
    text = "this is an example for huffman encoding"
    encoded, codes = huffman_encode(text)

    print(f"   Original: {text}")
    print(f"   Original size: {len(text) * 8} bits")
    print(f"   Encoded size: {len(encoded)} bits")
    print(f"   Compression: {calculate_compression_ratio(text, encoded):.1f}%")

    # Show codes
    print("\n2. Huffman Codes")
    sorted_codes = sorted(codes.items(), key=lambda x: len(x[1]))
    for char, code in sorted_codes[:5]:
        print(f"   '{char}': {code}")
    print("   ...")

    # Decode test
    print("\n3. Decode Test")
    decoded = huffman_decode(encoded, codes)
    print(f"   Decoded matches original: {decoded == text}")

    print("\n" + "=" * 60)
    print("All tests completed!")

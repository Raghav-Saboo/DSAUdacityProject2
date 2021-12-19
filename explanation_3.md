Huffman Coding


- Design
    - All the characters and their frequency is inserted in a min heap.
    - Binary tree is constructed using the top two elements from the min heap.
    - Path of each leaf provides the code for that character.
- Time Complexity
    - O(nlog(n)) for encoding and decoding
- Space Complexity
    - O(n) for storing the encoded and decoded text
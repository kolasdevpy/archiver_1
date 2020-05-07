# archiver
It's a small home project for learning of python and GitHub services.\
This project including writing simple algoritm and Its improvement.

________

# compression
The logic of the compression is to write sequences of identical bytes into two bytes and their counter.

For example:
- 2, 2, 2, 2, 2, 2 => 2, 2, 4
- 7, 9, 3, 3, 3, 3, 10, 11 => 7, 9, 3, 3, 2, 10, 11
- 3, 3 => 3, 3, 0 - this is a flaw in the algorithm

# decompression
The decompression logic is to find two identical consecutive bytes.\
The next byte is already a counter and lets you know how many of these bytes\ you still need to add to the unpacked sequences.

For example:
- 3, 3, 0 => 3, 3
- 2, 2, 1 => 2, 2, 2
- 0, 7, 7, 5, 11 => 0, 7, 7, 7, 7, 7, 7, 7, 11

________
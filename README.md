# archiver
It's a small home project for learning of python and GitHub services.\
This project including writing simple algoritm and Its improvement.

________

# compression
The logic of the compression is to write sequences of identical bytes into two bytes and their counter.

For example:
- 2, 2, 2, 2, 2, 2, 1, 3 => 2, 2, 4, 1, 3
- 1, 2, 3, 3, 3, 3, 4, 5 => 1, 2, 3, 3, 2, 4, 5
- 3, 3 => 3, 3, 0 - this is a flaw in the algorithm

# decompression
The decompression logic is to find two identical consecutive bytes.\
The next byte is already a counter and lets you know how many of these bytes you still need to add to the unpacked sequences.

For example:
- 3, 3, 0 => 3, 3
- 1, 2, 2, 1 => 1, 2, 2, 2
- 0, 7, 7, 5 => 0, 7, 7, 7, 7, 7, 7, 7

________
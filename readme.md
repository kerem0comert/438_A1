# Kerem Cömert 2315190

## Setup

Simply run the following command inside ./A1 :
`python main.py`

## Description

The code implements a Simple Cipher, with the help of a lookup table. A key is generated each
time a text is encrypted. The same key can be used to decrypt and get back the original plain text.
The code contains comments to explain my line of thinking in the implementation.

There are some useful functions I wrote, but I used Python's built-in methods for simple operations
like strip(), isUpper(), isLower() for code integrity. The program also makes use of regular
expressions to read the table from the file, as the txt was in C syntax.
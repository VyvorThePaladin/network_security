# Network Security

## Getting Started

+ [Install jupyter notebook](https://jupyter.readthedocs.io/en/latest/install.html)
+ Run the notebook: `jupyter notebook`
+ On mac: `/path/anaconda3/bin/jupyter_mac.command ; exit ;`
+ To convert to python file: `jupyter nbconvert --to script filename.ipynb`

## Cipher Implementations

+ #### Caesar Cipher
The Caesar cipher is one of the earliest known and simplest ciphers. It is a type of substitution cipher in which each letter in the plaintext is 'shifted' a certain number of places down the alphabet. A simple illustration is given where a hardcoded encrypted string is decrypted using Caesar cipher.

+ #### Feistel Cipher
The Feistel cipher is a symmetric structure used in the construction of block ciphers(symmetric key cipher i.e. both parties have same secret key, which operates on a groups of bits of fixed length, called blocks, using an exact transformation.), named after the German IBM cryptographer Horst Feistel.

+ #### Vigenère Cipher
Vigenere Cipher is a method of encrypting alphabetic text. It uses a simple form of polyalphabetic substitution. A polyalphabetic cipher is any cipher based on substitution, using multiple substitution alphabets .The encryption of the original text is done using the Vigenère square or Vigenère table.

+ #### Data Encryption Standard
The Data Encryption Standard (DES) is a symmetric-key block cipher published by the National Institute of Standards and Technology (NIST). DES is an implementation of a Feistel Cipher. It uses 16 round Feistel structure. The block size is 64-bit.

+ #### Advanced Encryption Standard
The advanced encryption standard (AES) is the current US standard in symmetric block ciphers. AES uses 128-bit (with 10 rounds of encryption), 192-bit (with 12 rounds of encryption), or 256-bit (with 14 rounds of encryption) keys to encrypt 128-bit blocks of data.

# Encrypt and decrypt message using columnar transposition cipher

import math


def encrypt(key, msg):
    """Encrypt a message using columnar transposition cipher.

    :param key: the key used to encrypt the message
    :type key: int

    :param msg: the message in plain text (before being encrypted)
    :type msg: str

    :return: a message in cipher text
    """

    ciphertext = [''] * key

    for column in range(key):
        current_index = column
        while current_index < len(msg):
            ciphertext[column] += msg[current_index]
            current_index += key
    return ''.join(ciphertext)


def decrypt(key, msg):
    """Decrypt a message using columnar transposition cipher.

    :param key: the key used to decrypt the message
    :type key: int

    :param msg: the message in cipher text (before being decrypted)
    :type msg: str

    :return: a message in plain text
    """

    num_columns = math.ceil(len(msg) / key)
    num_rows = key
    num_shaded_boxes = (num_columns * num_rows) - len(msg)
    plaintext = [''] * num_columns

    column = row = 0
    for symbol in msg:
        plaintext[column] += symbol
        column += 1
        if (column == num_columns
                or (column == num_columns - 1 and row >= num_rows - num_shaded_boxes)):
            column = 0
            row += 1
    return ''.join(plaintext)

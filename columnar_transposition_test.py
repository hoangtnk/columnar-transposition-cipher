#!/usr/bin/env python3
#
# Transposition Cipher Test

import random
import sys

from columnar_transposition_cipher import encrypt, decrypt


def main():
    """Auto test the columnar transposition cipher."""

    random.seed(42)

    for i in range(20):  # run 20 tests
        msg = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * random.randint(4, 40)
        msg = list(msg)
        random.shuffle(msg)
        msg = ''.join(msg)

        print('Test #{}: "{}..."'.format(i + 1, msg[:50]))

        for key in range(1, int(len(msg)/2)):
            encrypted = encrypt(key, msg)
            decrypted = decrypt(key, encrypted)
            if msg != decrypted:
                print("Mismatch with key {} and message {}".format(key, msg))
                print("Decrypted as: ".format(decrypted))
                sys.exit()

    print("Transposition cipher test passed.")


if __name__ == "__main__":
    main()

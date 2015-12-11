#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string

def crypt(key, msg):
    cipher = []
    i = 0
    for c in msg:
        if c in string.ascii_lowercase:
            pos_c = ord(c) - ord('a')
            pos_k = ord(key[i]) - ord('a')
            cipher.append(chr((pos_c + pos_k) % 26 + ord('a')))
            i = (i + 1) % len(key)
        else:
            cipher.append(c)
    return ''.join(cipher)

def decrypt(key, msg):
    cipher = []
    i = 0
    for c in msg:
        if c in string.ascii_lowercase:
            pos_c = ord(c) - ord('a')
            pos_k = ord(key[i]) - ord('a')
            cipher.append(chr((pos_c - pos_k) % 26 + ord('a')))
            i = (i + 1) % len(key)
        else:
            cipher.append(c)
    return ''.join(cipher)

"""
def crypt(key, plain):
    cipher = []
    i = 0
    for c in plain:
        if c in string.ascii_lowercase:
            pos_c = ord(c) - ord('a')
            pos_k = ord(key[i]) - ord('a')
            cipher.append(chr((pos_c + pos_k) % 26 + ord('a')))
            i = (i + 1) % len(key)
        else:
            cipher.append(c)
    return "".join(cipher)


def decrypt(key, cipher):
    plain = []
    i = 0
    for c in cipher:
        if c in string.ascii_lowercase:
            pos_c = ord(c) - ord('a')
            pos_k = ord(key[i]) - ord('a')
            plain.append(chr((pos_c - pos_k) % 26 + ord('a')))
            i = (i + 1) % len(key)
        else:
            plain.append(c)
    return "".join(plain)
"""

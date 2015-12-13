#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import vigenere_lib
import pso

if __name__ == '__main__':
    if len(sys.argv) != 4 or sys.argv[1] not in ["-enc", "-dec", "-pso"]:
        print("Usage:\t%s -enc|-dec plain_file key" % sys.argv[0])
        print("\t%s -pso cipher_file key_size nb_turn" % sys.argv[0])
        sys.exit(1)

    with open(sys.argv[2]) as f:
        data = f.read()

    if sys.argv[1] == "-enc":
        key = sys.argv[3]
        print(vigenere_lib.crypt(key, data))
    elif sys.argv[1] == "-dec":
        key = sys.argv[3]
        print(vigenere_lib.decrypt(key, data))
    elif sys.argv[1] == "-pso":
        key_size = int(sys.argv[3])
        pso.analyze(data.lower(), key_size)

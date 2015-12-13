#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import string
from language.en import words_list, letters_frequencies
import vigenere_lib


class VigenereIndividual:
    def __init__(self, cipher, key, index, letter):
        self._key = key[:]
        self._key[index] = letter
        self._cipher = cipher
        self._fitness = 0
        self.compute_fitness()

    @property
    def new_key(self):
        return self._key

    @property
    def fitness(self):
        return self._fitness

    def compute_fitness(self):
        plain = vigenere_lib.decrypt("".join(self._key), self._cipher)
        for w in words_list:
            self._fitness += plain.count(w)


def generate_individuals(cipher, key):
    individuals = list()
    for index in range(len(key)):
        for letter in string.ascii_lowercase:
            individuals.append(VigenereIndividual(cipher, key, index, letter))
    return individuals


def get_solution_from_individuals(individuals):
    individuals = sorted(individuals, key=lambda x: x.fitness, reverse=True)
    return individuals[0]


def analyze(data, key_size):
    key = [random.choice(string.ascii_lowercase) for _ in range(key_size)]
    while True:
        individuals = generate_individuals(data, key)
        solution = get_solution_from_individuals(individuals)
        if "".join(key) == "".join(solution.new_key):
            break
        key = solution.new_key
        print('Key=%s\t\tFitness=%d' % ("".join(key), solution.fitness))

    print("")
    print("Key=%s" % "".join(key))
    print(vigenere_lib.decrypt("".join(key), data))

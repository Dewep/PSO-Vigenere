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

    def compute_frequency(self, message, search):
        return round(message.count(search) / len(message) * 1000)

    def compute_fitness(self):
        plain = vigenere_lib.decrypt("".join(self._key), self._cipher)
        self._fitness = 10000
        for l in letters_frequencies:
            self._fitness += abs(letters_frequencies[l] - self.compute_frequency(plain, l))
        for w in words_list:
            self._fitness -= plain.count(w) * 20
        if self._fitness < 0:
            self._fitness = 0


def generate_individuals(cipher, key):
    individuals = list()
    for index in range(len(key)):
        for letter in string.ascii_lowercase:
            individuals.append(VigenereIndividual(cipher, key, index, letter))
    return individuals


def get_solution_from_individuals(individuals, nb_turn, turn):
    individuals = sorted(individuals, key=lambda x: x.fitness)
    fitness_list = []
    margin = (1 + 0.0005 * ((nb_turn - turn) * 100) / nb_turn)
    maximum = round(individuals[0].fitness * margin)
    for i in individuals:
        if i.fitness > maximum + 1:
            break
        fitness_list.append(i)
    return random.choice(fitness_list)


def analyze(data, key_size, nb_turn):
    key = [random.choice(string.ascii_lowercase) for _ in range(key_size)]
    for turn in range(nb_turn):
        individuals = generate_individuals(data, key)
        solution = get_solution_from_individuals(individuals, nb_turn, turn)
        key = solution.new_key
        print('Turn=%d\t\tKey=%s\t\tFitness=%d' % (turn, "".join(key), solution.fitness))

    print("")
    print("Key=%s" % "".join(key))
    print(vigenere_lib.decrypt("".join(key), data))

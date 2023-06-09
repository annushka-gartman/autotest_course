import random
import string


def random_string():
    string_random = ""
    for letter in random.sample(list(string.ascii_lowercase), random.randint(1, 15)):
        string_random = string_random + letter
    return string_random


def generate_random_name():
    while True:
        yield random_string() + " " + random_string()


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
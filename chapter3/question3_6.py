from collections import defaultdict

"""
class AnimalNode:
    def __init__(self, name, species):
        self.name = name
        self.species = species

        # Standard List poperties
        self.next = None
        self.prev = None

        # Next and Prev of species
        self.next_of_type = None
        self.prev_of_type = None


class AnimalList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, animal):
        if self.head is None:
            self.head = animal
            self.tail = animal
        else:
            self.tail.next = animal
            self.tail = animal

    def remove(self):
        if self.head:
            return_val = self.head
            self.head = self.head.next
            return_val.next = None

class AnimalOfType:
    def __init__(self):



class AnimalShelter:
    def __init__(self):
        self.animals = AnimalList()
        self.animals_by_type = defaultdict(AnimalList)


    def add(self, animal):
"""
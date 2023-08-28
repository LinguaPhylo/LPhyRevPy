from abc import ABC
from typing import List

from lphy.core.model.Function import DeterministicFunction
from lphy.core.model.Value import Value


class CreateTaxa(DeterministicFunction, ABC):

    generator_info = {"name": "taxa",
                      "description": "A set of taxa with species and ages defined in parallel arrays."}

    # TODO get rid of Value, so use names: List[str]
    def __init__(self, names: Value, species=None, ages=None):
        super().__init__()
        # have to take Value.value
        self.names = names.value
        if species is None:
            self.species = []
        else:
            self.species = species.value
        if ages is None:
            self.ages = []
        else:
            self.ages = ages.value

    def apply(self) -> "Value":
        taxon_list = []

        for i in range(len(self.names)):
            name = str(self.names[i])
            spec = None
            if self.species:
                spec = str(self.species[i])
            age = 0.0
            if self.ages:
                age = self.ages[i]

            taxon_list.append(Taxon(name, spec, age))

        taxa = Taxa(taxon_list)

        return Value(None, taxa, self)


class Taxon:
    def __init__(self, name, species=None, age=0.0):
        self.name = name
        self.species = species
        self.age = age

    def is_extant(self):
        return self.age == 0.0

    def set_species(self, species):
        self.species = species

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_species(self):
        if self.species is None:
            return self.name
        return self.species

    def __str__(self):
        if self.species is not None and self.species != self.name:
            return f"{self.name}/{self.species}={self.age}"
        return f"{self.name}={self.age}"


class Taxa:
    def __init__(self, taxon_list: List[Taxon]):
        self.taxon_list = taxon_list

    def n_taxa(self):
        return len(self.taxon_list)

    def get_taxon(self, i):
        return self.taxon_list[i]


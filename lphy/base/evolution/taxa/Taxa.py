from abc import ABC
from typing import List

from lphy.core.model.Function import DeterministicFunction, method_info
from lphy.core.model.Value import Value


class CreateTaxa(DeterministicFunction, ABC):

    generator_info = {"name": "taxa",
                      "description": "A set of taxa with species and ages defined in parallel arrays."}

    # TODO get rid of Value, so use names: List[str]
    def __init__(self, names: Value, species=None, ages=None):
        super().__init__()
        # deal with None later
        self.names = names
        self.species = species
        self.ages = ages
        if len(names.value) < 2:
            raise RuntimeError("The taxa must contain at least 1 taxon given by name")

    def apply(self) -> "Value":
        taxon_list = []
        names_list = self.names.value
        #TODO same len?
        species_list = [] if self.species is None else self.species.value
        ages_list = [] if self.ages is None else self.ages.value

        for i in range(len(names_list)):
            name = str(names_list[i])
            spec = None
            if species_list:
                spec = str(species_list[i])
            age = 0.0
            if ages_list:
                age = ages_list[i]

            taxon_list.append(Taxon(name, spec, age))

        taxa = Taxa(taxon_list)

        return Value(None, taxa, self)

    # overwrite to F so only print the for loop, without taxa :=
    def is_rev_assignment(self):
        return False

    def lphy_to_rev(self, var_name):
        names_list = self.names.value
        var_nm = "i"
        # for (i in 1:10) { taxa[i] = taxon("Taxon"+i) }
        return f"""for ({var_nm} in 1:{len(names_list)}) {{ {var_name}[{var_nm}] = taxon({var_nm}) }} """

    # def method_call_to_rev(self, method_name: str, args):
    #     if method_name == "taxaNames":
    #         # for (i in 1:10) { taxa[i] = taxon("Taxon"+i) }
    #         return f"""for ({var_nm} in 1:{len(names_list)}) {{ taxa[{var_nm}] = taxon({var_nm}) }} """


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

    def __init__(self, taxon_list=None):
        if taxon_list is None:
            taxon_list = []
        self.taxon_list = taxon_list

    @method_info("The names of the taxa.")
    def taxaNames(self):
        pass

    @method_info("gets the ages of these taxa as an array of doubles.")
    def ages(self):
        pass

    @method_info("gets the number of taxa.")
    def length(self):
        return self.n_taxa()

    def n_taxa(self):
        return len(self.taxon_list)

    def get_taxon(self, i):
        return self.taxon_list[i]


from abc import ABC
from typing import List, Dict

from lphy.core.model.Function import DeterministicFunction, method_info
from lphy.core.model.Value import Value


def create_n_taxa(n: int, var_name: str, loop_var_name="i"):
    """
    :return: a Rev for loop to create n taxa with name from 1 to n
    """
    taxa_var_name = var_name + "_taxa"
    # for (i in 1:10) { taxa[i] = taxon("Taxon"+i) }
    return f"""for ({loop_var_name} in 1:{n}) {{ {taxa_var_name}[{loop_var_name}] = taxon({loop_var_name}) }} """


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
        # TODO same len?
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
    def has_var_declaration_rev(self):
        return False

    def lphy_to_rev(self, var_name):
        names_list = self.names.value
        loop_var = "i"
        # for (i in 1:10) { taxa[i] = taxon("Taxon"+i) }
        return f"""for ({loop_var} in 1:{len(names_list)}) {{ {var_name}[{loop_var}] = taxon({loop_var}) }} """

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

    def __init__(self, taxon_list: List[Taxon] = None):
        self.taxon_list = taxon_list

    @method_info("The names of the taxa.")
    def taxaNames(self):
        return self.get_taxa_names()

    @method_info("gets the ages of these taxa as an array of doubles.")
    def ages(self):
        return self.get_ages()

    @method_info("gets the species of these taxa as an array of doubles.")
    def species(self):
        return self.get_species()

    @method_info("gets the number of taxa.")
    def length(self):
        return self.n_taxa()

    def n_taxa(self):
        return len(self.taxon_list)

    def get_taxon(self, i):
        return self.taxon_list[i]

    def get_taxa_names(self):
        if self.taxon_list:
            return [taxon.get_name() for taxon in self.taxon_list]
        return []

    def index_of_taxon(self, taxon_name: str):
        names = self.get_taxa_names()
        for i in range(len(names)):
            if names[i] == taxon_name:
                return i
        return -1

    def get_ages(self):
        if self.taxon_list:
            return [taxon.get_age() for taxon in self.taxon_list]
        return []

    def get_species(self):
        if self.taxon_list:
            return [taxon.get_species() for taxon in self.taxon_list]
        return []


def create_taxa(taxon_list: List[Taxon]) -> Taxa:
    return Taxa(taxon_list)


def create_taxa_by_objects(objects: List) -> Taxa:
    taxa = [Taxon(str(obj), age=0.0) for obj in objects]
    return Taxa(taxa)


def create_taxa_by_ages(ages: List) -> Taxa:
    taxa = [Taxon(str(i), age=ages[i]) for i in range(len(ages))]
    return Taxa(taxa)


def create_taxa_by_n(n: int) -> Taxa:
    taxa = [Taxon(str(i), age=0.0) for i in range(n)]
    return Taxa(taxa)


# key is String, value is Integer
def create_taxa_by_id_map(id_map: Dict) -> Taxa:
    if not id_map or len(id_map) < 2:
        raise ValueError(f"Invalid id map that has no values : {id_map}")

    taxa: List[Taxon] = [None] * len(id_map)
    for name, index in id_map.items():
        if 0 <= index < len(taxa):
            taxa[index] = Taxon(name)
        else:
            raise ValueError(f"Index {index} for taxon '{name}' is out of range.")

    return Taxa(taxa)


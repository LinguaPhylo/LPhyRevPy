import logging
from abc import ABC
from lphy.base.evolution.alignment.Alignment import Alignment
from lphy.core.model.Function import DeterministicFunction
from lphy.core.model.Value import Value


class ReadFasta(DeterministicFunction, ABC):

    generator_info = {"name": "readFasta",
                      "description": "A function that parses an alignment from a fasta file."}

    def __init__(self, file: Value, options=None):
        super().__init__()
        # deal with None later
        self.file = file
        self.options = options
        # TODO how to handle options?
        if options is not None:
            logging.warning(f"Options in {self.generator_info['name']} is ignored, options = {options}")


    def apply(self) -> "Value":
        #TODO Alignment?
        return Value(None, Alignment(), self)

    # D <- readDiscreteCharacterData("data/horses_isochronous_sequences.fasta")
    def rev_spec_op(self) -> str:
        return '<-'

    def lphy_to_rev(self, var_name):
        #TODO how to handle options?
        return f"""readDiscreteCharacterData("{self.file}")"""


# https://revbayes.github.io/tutorials/ctmc/
class ReadNexus(DeterministicFunction, ABC):
    """
    Rev does not fully support Nexus format, such as codons, and Nucleotide data type (must be DNA)
    """
    generator_info = {"name": "readNexus",
                      "description": "A function that parses an alignment from a Nexus file."}

    def __init__(self, file: Value, options=None):
        super().__init__()
        # deal with None later
        self.file = file
        self.options = options
        # TODO how to handle options?
        if options is not None:
            logging.warning(f"Options in {self.generator_info['name']} is ignored, options = {options}")

    def apply(self) -> "Value":
        # TODO Alignment?
        return Value(None, Alignment(), self)

    # data <- readDiscreteCharacterData("data/primates_and_galeopterus_cytb.nex")
    def rev_spec_op(self) -> str:
        return '<-'

    def lphy_to_rev(self, var_name):
        # TODO how to handle options?
        return f"""readDiscreteCharacterData("{self.file}")"""

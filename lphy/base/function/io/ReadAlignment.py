import logging
from abc import ABC

from lphy.base.evolution.SequenceType import SequenceType, Nucleotide
from lphy.base.evolution.taxa.Taxa import Taxon, create_taxa, Taxa
from lphy.base.evolution.alignment.Alignment import Alignment
from lphy.core.model.Function import DeterministicFunction
from lphy.core.model.Value import Value
from Bio import SeqIO


# Bio.AlignIO.FastaIO
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

        file_path = self.file.value

        # TODO options

        sequence_type : SequenceType = Nucleotide();
        taxon_list = []
        state_num_list_list = []
        site_count = 0

        for seq in SeqIO.parse(file_path, "fasta"):
            taxon_list.append(Taxon(seq.id))
            # must be upper case
            j = seq.seq.upper()
            # convert A,C,G,T to int
            state_num_list = sequence_type.get_states(j)
            # 2d here
            state_num_list_list.append(state_num_list)

            if site_count <= 0:
                site_count = len(seq)
            elif site_count != len(seq):
                logging.warning(f"{file_path} contain a sequence {seq.id} not match the length ({site_count}) "
                                f"of other sequences !")

        taxa: Taxa = create_taxa(taxon_list)
        alig = Alignment(taxa, site_count) #TODO deafult to DNA now

        for i in range(len(state_num_list_list)):
            # a list of int
            state_num_list = state_num_list_list[i]
            for j in range(len(state_num_list)):
                # Set the state number in the NumPy array
                alig.set_state(i, j, state_num_list[j])

        return Value(None, alig, self)

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

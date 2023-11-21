import re
from typing import Dict

import numpy as np

from lphy.base.evolution.SequenceType import SequenceType, Nucleotide
from lphy.base.evolution.taxa.Taxa import Taxa, create_taxa_by_id_map, Taxon
from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.model.Function import method_info


def parse_charset(charset: str):
    #TODO hard code
    #codon_str = ["1-.\3", "2-.\3", "3-.\3"]

    # Regular expression pattern to match the given string
    regx = re.compile(r"([1-3])-\\.\\3")
    result = regx.match(charset)
    if result:
        return result.group(1)
    return None


class Alignment(Taxa):

    @method_info("The number of characters/sites.")
    def nchar(self):
        return self.nchar

    @method_info("the taxa of the alignment.")
    def taxa(self) -> Taxa:
        return self.get_taxa()

    @method_info("The names of the taxa.")
    def getTaxaNames(self):
        return self.get_taxa_names()

    @method_info("get the data type of this alignment.")
    def dataType(self):
        return self.sequence_type

    @method_info("get the data type of this alignment.")
    def charset(self, charset: str):
        return parse_charset(charset)

    def method_call_to_rev(self, method_name: str, args):
        if method_name == "nchar":
            return f"nchar()"
        elif method_name == "taxa":
            return f"taxa()"
        elif method_name == "taxaNames":  # Rev taxa has no names()
            return f"names()"
        elif method_name == "charset":  # D.setCodonPartition(1)
            return f"setCodonPartition({args})"
        else:
            raise UnsupportedOperationException("")

    VAR_SITE_STATE = -1  # TODO for marking the constant sites.

    # TODO only available to DNA now
    def __init__(self, taxa_or_id_map, nchar, sequence_type: SequenceType = Nucleotide()):
        super().__init__()
        if isinstance(taxa_or_id_map, dict):
            self.taxa = create_taxa_by_id_map(taxa_or_id_map)
        elif isinstance(taxa_or_id_map, Taxa):
            self.taxa = taxa_or_id_map
        else:
            raise ValueError("It must be either taxon id dict or taxa object !")
        self.nchar = nchar
        self.sequence_type = sequence_type  # default to DNA

        # Create a NumPy 2D array filled with zeros
        self.alignment = np.zeros((self.n_taxa(), self.nchar), dtype=int)
        self.constant_sites_mark = None

    def n_taxa(self):
        return self.taxa.n_taxa()

    def get_taxa(self) -> Taxa:
        return self.taxa

    def get_taxon(self, index: int) -> Taxon:
        return self.taxa.get_taxon(index)

    def get_taxa_names(self):
        return self.taxa.get_taxa_names()

    def get_taxon_name(self, index: int):
        return self.get_taxon(index).get_name()

    def set_state(self, taxon_index: int, position: int, state):
        if self.sequence_type is None:
            raise ValueError("Please define SequenceType, not numStates!")
        if state < 0 or state > self.sequence_type.get_state_count():
            raise ValueError(
                f"Illegal to set a {self.sequence_type.__class__} state outside of "
                f"the range [0, {self.sequence_type.get_state_count() - 1}]! state = {state}")
        self.alignment[taxon_index][position] = state

    def set_state_by_taxon_name(self, taxon_name, position, state):
        taxon = self.index_of_taxon(taxon_name)
        self.set_state(taxon, position, state)

    def get_state(self, taxon, position):
        return self.alignment[taxon][position]

    def get_sequence(self, taxon_index):
        sequence = ""
        # state is int
        for state in self.alignment[taxon_index]:
            sequence += self.sequence_type.get_state_code(state)
        return sequence

    # TODO to check or not need?
    def get_constant_sites_mark(self):
        if self.constant_sites_mark is not None:
            return self.constant_sites_mark
        if len(self.alignment) != self.n_taxa() or len(self.alignment[0]) != self.nchar:
            raise ValueError(f"Illegal alignment: {len(self.alignment)} != "
                             f"{self.n_taxa()}, {len(self.alignment[0])} != {self.nchar}")

        self.constant_sites_mark = [0] * self.nchar
        for i in range(self.nchar):
            is_constant = True
            first_state = self.get_state(0, i)
            for t in range(1, self.n_taxa()):
                tmp = self.get_state(t, i)
                if tmp < 0:
                    raise ValueError(f"Illegal state {tmp} in {self.get_taxon_name(t)} sequence!")
                if tmp != first_state:
                    is_constant = False
                    break
            if is_constant:
                self.constant_sites_mark[i] = first_state
            else:
                self.constant_sites_mark[i] = self.VAR_SITE_STATE
        if all(m == self.VAR_SITE_STATE for m in self.constant_sites_mark):
            self.constant_sites_mark = []

        return self.constant_sites_mark

    def has_constant_site(self):
        return self.constant_sites_mark is not None and len(self.constant_sites_mark) > 0

    def get_sequence_var_site(self, taxon_index):
        if not self.has_constant_site():
            return self.get_sequence(taxon_index)
        sequence = ""
        mark = self.get_constant_sites_mark()
        for j in range(len(self.alignment[taxon_index])):
            if mark[j] == self.VAR_SITE_STATE:
                sequence += self.sequence_type.get_state_code(self.alignment[taxon_index][j])
        return sequence


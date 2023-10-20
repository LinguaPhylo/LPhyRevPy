from abc import abstractmethod
from typing import List


class SequenceType:
    @abstractmethod
    def get_states(self, sequence_str: str) -> List:
        pass

    @abstractmethod
    def get_state_code(self, state_index):
        pass

    @abstractmethod
    def get_state_index(self, state_code):
        pass

    @abstractmethod
    def get_state_count(self):
        pass

    @abstractmethod
    def get_canonical_state_count(self):
        pass

    # codons are 3
    def get_code_length(self):
        return 1


class Nucleotide(SequenceType):

    dna_to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3,
                  # A/G    C/T    A/C     A/T     C/G     G/T     C/G/T    A/G/T    A/C/T    A/C/G
                  'R': 4, 'Y': 5, 'M': 6, 'W': 7, 'S': 8, 'K': 9, 'B': 10, 'D': 11, 'H': 12, 'V': 13,
                  # Unknown         gap
                  'N': 14, '?': 15, '-': 16}

    # Convert the upper case sequences into a list of integer states
    def get_states(self, sequence_str: str) -> List:
        return [self.dna_to_int[base] for base in sequence_str]

    def get_state_code(self, state_index):
        return list(self.dna_to_int.keys())[state_index]

    def get_state_index(self, state_code):
        return self.dna_to_int[state_code]

    # 17
    def get_state_count(self):
        return len(self.dna_to_int)

    # 4
    def get_canonical_state_count(self):
        return 4

# class AminoAcids(SequenceType):
#
#
#
# class Binary(SequenceType):
#
#
#
# class Standard(SequenceType):




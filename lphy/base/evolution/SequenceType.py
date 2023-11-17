from abc import abstractmethod
from typing import List


class SequenceType:
    @abstractmethod
    def get_states(self, sequence_str: str) -> List:
        pass

    @abstractmethod
    def get_state_code(self, state_index: int) -> str:
        pass

    @abstractmethod
    def get_state_index(self, state_code: str) -> int:
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
    # total 17     0 ,  1 ,  2,   3,  A/G  C/T  A/C  A/T  C/G  G/T  C/G/T A/G/T A/C/T A/C/G
    dna_to_int = ['A', 'C', 'G', 'T', 'R', 'Y', 'M', 'W', 'S', 'K',  'B',  'D',  'H',  'V',
    # 14 15  Unknown       16 gap
                 'N', '?', '-']

    # Convert the upper case sequences into a list of integer states
    def get_states(self, sequence_str: str) -> List:
        return [self.get_state_index(char) for index, char in enumerate(sequence_str)]

    def get_state_code(self, state_index: int) -> str:
        return self.dna_to_int[state_index]

    def get_state_index(self, state_code: str) -> int:
        # Return first index of value. Raises ValueError if the value is not present.
        return self.dna_to_int.index(state_code)

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




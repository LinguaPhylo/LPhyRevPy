from abc import ABC
from typing import List, Optional

from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.Value import Value
from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.model.Function import method_info
from lphy.base.evolution.taxa.Taxa import Taxa, Taxon, create_taxa_by_n, create_taxa_by_ages, create_taxa, \
    create_taxa_by_objects
from lphy.base.evolution.tree.TimeTree import TimeTree
from lphy.base.evolution.tree.TimeTreeNode import TimeTreeNode

import random


def draw_random_node(node_list: List):
    # Java int value between 0 (inclusive) and n (exclusive).
    # Here range [a, b], including both end points.
    return node_list.pop(random.randint(0, len(node_list) - 2))


class TaxaConditionedTreeGenerator(GenerativeDistribution, ABC):

    def __init__(self, n: Value, taxa_value: Value, ages: Value):
        super().__init__()
        self.n = n
        self.taxa_value = taxa_value
        self.ages = ages

        # taxa is the value wrapped inside Value taxa_value
        # call construct_taxa
        self.taxa: Optional[Taxa] = None

    def construct_taxa(self) -> Taxa:
        if not self.taxa_value:
            # taxa_value has no value
            if self.ages:
                # create taxa from ages
                self.taxa = create_taxa_by_ages(self.ages.value)
            else:
                self.taxa = create_taxa_by_n(self.get_n())

        elif isinstance(self.taxa_value.value, Taxa):
            self.taxa = self.taxa_value.value

        elif isinstance(self.taxa_value.value, List):
            if all(isinstance(item, Taxon) for item in self.taxa_value.value):
                # create Taxa from taxon_list
                self.taxa = create_taxa(self.taxa_value.value)
            else:
                # create Taxa from object_list
                self.taxa = create_taxa_by_objects(self.taxa_value.value)
        else:
            raise ValueError(
                f"taxa must be of type List[Taxon] or Taxa, but it is type {type(self.taxa_value.value)}.")

    def get_taxa(self) -> Taxa:
        if not self.taxa:
            self.construct_taxa()
        return self.taxa

    def get_n(self):
        if self.n:
            return self.n
        return self.get_taxa().n_taxa()

    def create_leaf_nodes(self, tree: TimeTree) -> List[TimeTreeNode]:
        if not self.taxa:
            self.construct_taxa()
        names = self.taxa.get_taxa_names()
        ages = self.taxa.get_ages()

        node_list = []
        for i in range(len(names)):
            node = TimeTreeNode(names[i], tree)
            node.set_age(ages[i])
            node.set_leaf_index(i)
            node_list.append(node)
        return node_list

    def create_leaf_taxa(self, tree: TimeTree) -> List[TimeTreeNode]:
        return self.create_leaf_nodes(tree)

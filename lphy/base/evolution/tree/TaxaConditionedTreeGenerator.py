from abc import ABC
from typing import List, Optional

from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.Value import Value
from lphy.base.evolution.taxa.Taxa import Taxa, Taxon, create_taxa_by_n, create_taxa_by_ages, create_taxa, \
    create_taxa_by_objects
from lphy.base.evolution.tree.TimeTree import TimeTree
from lphy.base.evolution.tree.TimeTreeNode import TimeTreeNode

import random


def draw_random_node(node_list: List):
    # Java int value between 0 (inclusive) and n (exclusive).
    # Here range [a, b], including both end points.
    # nodeList.remove(random.nextInt(nodeList.size())) returns
    # the removed element previously at the specified position

    # Generate a random index within the range of the list
    #random_index = random.randint(0, len(node_list) - 1)
    # Remove the element at the random index
    #removed_element = node_list.pop(random_index)

    random_index = random.randrange(len(node_list))
    return node_list.pop(random_index)


class TaxaConditionedTreeGenerator(GenerativeDistribution, ABC):

    def __init__(self, n: Value, taxa_value: Value, ages: Value):
        super().__init__()
        self.n = n
        self.taxa = taxa_value  # self.taxa is reserved to Value wrapping taxa obj
        self.ages = ages

        # taxa_obj is the value wrapped inside Value taxa_value
        self.taxa_obj: Optional[Taxa] = None

    def check_taxa_parameters(self, at_least_one_required: bool):
        if at_least_one_required and self.taxa is None and self.n is None and self.ages is None:
            raise ValueError(f"At least one of 'n', 'taxa', 'ages' must be specified.")

        if self.taxa is not None and self.n is not None:
            t = self.get_taxa()
            if t.n_taxa() != self.n.value():
                raise ValueError(f"'n' and 'taxa' values are incompatible.")

        if self.ages is not None and self.n is not None:
            if len(self.ages.value()) != self.n.value():
                raise ValueError(f"'n' and 'ages' values are incompatible.")

        if self.ages is not None and self.taxa is not None:
            raise ValueError(f"Only one of 'taxa' and 'ages' may be specified.")

    def construct_taxa(self):
        """
        This fills in taxa_obj: Taxa
        """
        if not self.taxa:
            # taxa_value has no value
            if self.ages:
                # create taxa from ages
                self.taxa_obj = create_taxa_by_ages(self.ages.value)
            else:
                self.taxa_obj = create_taxa_by_n(self.get_n())

        elif isinstance(self.taxa.value, Taxa):
            self.taxa_obj = self.taxa.value

        elif isinstance(self.taxa.value, List):
            if all(isinstance(item, Taxon) for item in self.taxa.value):
                # create Taxa from taxon_list
                self.taxa_obj = create_taxa(self.taxa.value)
            else:
                # create Taxa from object_list
                self.taxa_obj = create_taxa_by_objects(self.taxa.value)
        else:
            raise ValueError(
                f"taxa must be of type List[Taxon] or Taxa, but it is type {type(self.taxa.value)}.")

    def get_taxa(self) -> Taxa:
        if not self.taxa_obj:
            self.construct_taxa()
        # validate taxa_obj: Taxa
        if not self.taxa_obj or self.taxa_obj.n_taxa() < 2:
            raise RuntimeError("It must have at least 2 taxa to construct a tree !")
        return self.taxa_obj

    def get_n(self):
        if self.n:
            return self.n.value
        return self.get_taxa().n_taxa()

    def create_leaf_nodes(self, tree: TimeTree) -> List[TimeTreeNode]:
        if not self.taxa_obj:
            self.construct_taxa()
        names = self.taxa_obj.get_taxa_names()
        ages = self.taxa_obj.get_ages()

        node_list = []
        for i in range(len(names)):
            node = TimeTreeNode(names[i], tree)
            node.set_age(ages[i])
            node.set_leaf_index(i)
            node_list.append(node)
        return node_list

    def create_leaf_taxa(self, tree: TimeTree) -> List[TimeTreeNode]:
        return self.create_leaf_nodes(tree)

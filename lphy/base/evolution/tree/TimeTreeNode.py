from typing import List

from lphy.base.evolution.taxa.Taxa import Taxon
from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.model.Function import method_info


class TimeTreeNode:
    ZERO_BRANCH_LENGTH_TOLERANCE = 1e-15

    parent = None
    index = 0
    leaf_index = -1
    meta_data = {}

    def __init__(self, *args):
        from lphy.base.evolution.tree.TimeTree import TimeTree
        if len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], TimeTree):
            # Constructor with (id, TimeTree)
            self.id_ = args[0]
            self.tree = args[1]
            self.age = 0.0
        elif len(args) == 1 and isinstance(args[0], (int, float)):
            # Constructor with (age)
            self.age = args[0]
        elif len(args) == 2 and isinstance(args[0], (int, float)) and isinstance(args[1], list):
            # Constructor with (age, children)
            self.age = args[0]
            self.children = args[1]
            for child in self.children:
                child.parent = self
        elif len(args) == 2 and isinstance(args[0], Taxon) and isinstance(args[1], TimeTree):
            # Constructor with (Taxon, TimeTree)
            taxon, tree = args
            self.age = taxon.getAge()
            self.id_ = taxon.getName()
            self.tree = tree
        else:
            raise ValueError("Invalid arguments for TimeTreeNode constructor")


    # def deep_copy(self, tree):
    #     copy = TimeTreeNode(self.id_, self.age, [])
    #     copy.index = self.index
    #     copy.leaf_index = self.leaf_index
    #     for child in self.children:
    #         copy.add_child(child.deep_copy(tree))
    #     return copy

    def is_root(self):
        return self.parent is None

    def is_origin(self):
        return self.parent is None and self.get_child_count() == 1

    def is_single_child_non_origin(self):
        return self.parent is not None and self.get_child_count() == 1

    def is_direct_ancestor(self):
        return self.is_single_child_non_origin() or (
                self.is_leaf() and (self.get_parent().age - self.age) <= self.ZERO_BRANCH_LENGTH_TOLERANCE)

    def is_leaf(self):
        return len(self.children) == 0

    def get_age(self):
        return self.age

    def get_children(self):
        return self.children

    def get_id(self):
        return self.id_

    def set_branch_rate(self, rate):
        self.set_meta_data("rate", rate)

    def get_branch_rate(self):
        return self.get_meta_data("rate")

    def set_meta_data(self, key, value):
        self.meta_data[key] = value

    def get_meta_data(self, key):
        return self.meta_data.get(key, None)

    def remove_meta_data(self, key):
        if key in self.meta_data:
            del self.meta_data[key]

    def get_all_leaf_nodes(self):
        leaf_nodes = []
        if not self.is_leaf():
            self.get_all_leaf_nodes_recursive(leaf_nodes)
        return leaf_nodes

    def get_all_leaf_nodes_recursive(self, leaf_nodes):
        if self.is_leaf():
            leaf_nodes.append(self)
        if not self.is_leaf():
            for child in self.children:
                child.get_all_leaf_nodes_recursive(leaf_nodes)

    def sort(self):
        if not self.is_leaf():
            for child in self.children:
                child.sort()
            self.children.sort(key=lambda x: x.index)

    def get_total_descendant_node_count(self):
        count = 1
        if self.is_leaf():
            return count
        for child in self.children:
            count += child.get_total_descendant_node_count()
        return count

    def get_child(self, i):
        if self.index >= 0 and i < len(self.children):
            return self.children[i]
        return None

    def get_left(self):
        if not self.is_leaf():
            return self.children[0] if len(self.children) > 0 else None
        return None

    def get_right(self):
        if not self.is_leaf():
            return self.children[1] if len(self.children) > 1 else None
        return None

    def set_left(self, left):
        if len(self.children) > 0:
            self.children[0] = left
            left.set_parent(self)
        else:
            self.add_child(left)

    def set_right(self, right):
        if len(self.children) > 1:
            self.children[1] = right
        else:
            if len(self.children) < 1:
                self.add_child(None)
            self.children.append(right)
        right.set_parent(self)

    def count_leaves(self):
        if self.is_leaf():
            return 1
        leaf_count = 0
        for child in self.get_children():
            leaf_count += child.count_leaves()
        return leaf_count

    def get_branch_duration(self):
        if not self.is_root():
            return self.get_parent().age - self.age
        return 0.0

    def is_extant(self):
        return self.is_leaf() and self.age == 0.0

    def add_child(self, child):
        self.children.append(child)
        if child is not None:
            child.set_parent(self)

    def remove_child(self, child):
        child.set_parent(None)
        self.children.remove(child)

    def set_age(self, age):
        self.age = age

    def set_id(self, id):
        self.id_ = id

    def get_child_count(self):
        return len(self.children)

    def get_parent(self):
        return self.parent

    def set_parent(self, new_parent):
        self.parent = new_parent

    def __str__(self):
        if self.is_leaf():
            return self.get_id()
        return super.__str__()

    def get_index(self):
        return self.index

    def set_index(self, index):
        self.index = index

    def get_leaf_index(self):
        return self.leaf_index

    def set_leaf_index(self, index):
        self.leaf_index = index

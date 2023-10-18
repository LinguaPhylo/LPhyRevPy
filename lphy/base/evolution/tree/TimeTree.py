from typing import List

from lphy.base.evolution.taxa.Taxa import Taxa, Taxon
from lphy.base.evolution.tree.TimeTreeNode import TimeTreeNode
from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.model.Function import method_info


def create_taxa(root: TimeTreeNode):
    taxa = [None] * root.count_leaves()
    collect_taxon(root, taxa)
    return Taxa(taxa)


def collect_taxon(node: TimeTreeNode, taxa: List[Taxon]):
    """
    Recursive add Taxon (leaf nodes) into taxa list,
    the position of Taxon in the list will be same as the node index
    """
    if node.is_leaf():
        taxa[node.get_index()] = Taxon(node.get_id(), age=node.get_age())
    else:
        for child in node.get_children():
            collect_taxon(child, taxa)


class TimeTree:
    def __init__(self, taxa=None):
        self.taxa = taxa

        self.root_node = None
        self.nodes: List[TimeTreeNode] = []
        self.n = 0

    def set_root(self, root: TimeTreeNode, reindex_leaves=False):
        self.root_node = root
        self.root_node.parent = None
        self.root_node.tree = self

        self.nodes = []
        self.fill_node_list(self.root_node, reindex_leaves)
        self._index_nodes(self.root_node, [self.n])

        self.nodes.sort(key=lambda node: node.index)
        if self.taxa is None:
            self.taxa = create_taxa(self.root_node)

    def _index_nodes(self, node: TimeTreeNode, next_internal_index):
        if node.is_leaf():
            node.set_index(node.get_leaf_index())
        else:
            for child in node.get_children():
                self._index_nodes(child, next_internal_index)
            node.set_index(next_internal_index[0])
            next_internal_index[0] += 1

    def get_single_child_node_count(self):
        return sum(1 for node in self.nodes if len(node.children) == 1)

    def fill_node_list(self, node, reindex_leaves):
        if node.is_root():
            self.nodes.clear()
            self.n = 0

        node.tree = self

        if "remove" in node.meta_data:
            raise RuntimeError(f"A node that should be removed has not been! {node.id_}")

        if node.is_leaf():
            self.nodes.append(node)
            if node.leaf_index == -1 or reindex_leaves:
                node.leaf_index = self.n
            self.n += 1
        else:
            for child in node.children:
                self.fill_node_list(child, reindex_leaves)
            self.nodes.append(node)

    def to_newick(self, include_single_child_nodes):
        builder = []
        self.to_newick_recursive(self.root_node, builder, include_single_child_nodes)
        return "".join(builder)

    def to_newick_recursive(self, node, builder, include_single_child_nodes):
        if not include_single_child_nodes and len(node.children) == 1:
            self.to_newick_recursive(node.children[0], builder, include_single_child_nodes)
        else:
            if node.is_leaf():
                builder.append(node.id_)
                meta_data = node.meta_data
                if len(meta_data) > 0:
                    builder.append("[&")
                    for key, value in meta_data.items():
                        builder.append(f"{key}={value}")
                    builder.append("]")
            else:
                builder.append("(")
                children = node.children
                self.to_newick_recursive(children[0], builder, include_single_child_nodes)
                for child in children[1:]:
                    builder.append(",")
                    self.to_newick_recursive(child, builder, include_single_child_nodes)
                builder.append(")")
            if node.is_root():
                builder.append(":0.0;")
            else:
                builder.append(f":{self.get_branch_length(node, include_single_child_nodes)}")

    def get_branch_length(self, node, include_single_child_nodes):
        parent = node.parent
        if not include_single_child_nodes:
            if len(parent.children) == 1:
                parent = parent.parent
        if parent is not None:
            return parent.age - node.age
        return 0.0

    def get_root(self) -> TimeTreeNode:
        return self.root_node

    def get_taxa_names(self):
        return self.taxa.get_taxa_names()

    def get_species(self):
        return self.taxa.get_species()

    def get_node_by_index(self, index):
        node = self.nodes[index]
        if node.index != index:
            raise RuntimeError()
        return node

    def is_ultrametric(self):
        for node in self.nodes:
            if node.is_leaf() and node.age != 0.0:
                return False
        return True

    def get_taxa(self):
        return self.taxa

    def get_extant_nodes(self):
        return [node for node in self.nodes if node.is_extant()]

    def get_internal_nodes(self):
        return [node for node in self.nodes if not node.is_extant()]

    def has_origin(self):
        return self.root_node.is_origin()

    @method_info("the total length of the tree")
    def treeLength(self):
        TL = 0.0
        for node in self.nodes:
            if not node.is_root():
                TL += node.parent.age - node.age
        return TL

    @method_info("the age of the root of the tree.")
    def rootAge(self):
        return self.get_root().age

    @method_info("the total number of nodes in the tree (both leaf nodes and internal nodes).")
    def nodeCount(self):
        return len(self.nodes)

    @method_info("the total number of branches in the tree (returns nodeCount() - 1).")
    def branchCount(self):
        return len(self.nodes) - 1

    @method_info("the total number of leaf nodes in the tree (leaf nodes with any age, "
                 "but excluding zero-branch-length leaf nodes, which are logically direct ancestors).")
    def leafCount(self):
        count = 0
        for node in self.nodes:
            if node.is_leaf() and not node.is_direct_ancestor():
                count += 1
        return count

    @method_info("the total number of extant leaves in the tree (leaf nodes with age 0.0).")
    def extantCount(self):
        count = 0
        for node in self.nodes:
            if node.age == 0.0 and node.is_leaf():
                count += 1
        return count

    def method_call_to_rev(self, method_name: str, args):
        # TODO more methods
        if method_name == "treeLength":
            return f"treeLength()"
        elif method_name == "rootAge":
            return f"rootAge()"
        elif method_name == "nodeCount":
            return f"nnodes()"
        elif method_name == "leafCount":
            return f"ntips()"
        else:
            raise UnsupportedOperationException("")

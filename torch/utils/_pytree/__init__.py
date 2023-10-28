"""
Contains utility functions for working with nested python data structures.

A *pytree* is Python nested data structure. It is a tree in the sense that
nodes are Python collections (e.g., list, tuple, dict) and the leaves are
Python values. Furthermore, a pytree should not contain reference cycles.

pytrees are useful for working with nested collections of Tensors. For example,
one can use `tree_map` to map a function over all Tensors inside some nested
collection of Tensors and `tree_leaves` to get a flat list of all Tensors
inside some nested collection. pytrees are helpful for implementing nested
collection support for PyTorch APIs.
"""


from .api import (
    _broadcast_to_and_flatten as _broadcast_to_and_flatten,
    _register_pytree_node as _register_pytree_node,
    Context as Context,
    DumpableContext as DumpableContext,
    FlattenFunc as FlattenFunc,
    FromDumpableContextFn as FromDumpableContextFn,
    LeafSpec as LeafSpec,
    PyTree as PyTree,
    SUPPORTED_NODES as SUPPORTED_NODES,
    ToDumpableContextFn as ToDumpableContextFn,
    tree_all as tree_all,
    tree_all_only as tree_all_only,
    tree_any as tree_any,
    tree_any_only as tree_any_only,
    tree_flatten as tree_flatten,
    tree_leaves as tree_leaves,
    tree_map as tree_map,
    tree_map_ as tree_map_,
    tree_map_only as tree_map_only,
    tree_map_only_ as tree_map_only_,
    tree_structure as tree_structure,
    tree_unflatten as tree_unflatten,
    TreeSpec as TreeSpec,
    treespec_dumps as treespec_dumps,
    treespec_loads as treespec_loads,
    treespec_pprint as treespec_pprint,
    UnflattenFunc as UnflattenFunc,
)


__all__ = [
    "PyTree",
    "TreeSpec",
    "LeafSpec",
    "Context",
    "FlattenFunc",
    "UnflattenFunc",
    "DumpableContext",
    "ToDumpableContextFn",
    "FromDumpableContextFn",
    "_register_pytree_node",
    "SUPPORTED_NODES",
    "tree_flatten",
    "tree_unflatten",
    "tree_leaves",
    "tree_structure",
    "tree_map",
    "tree_map_",
    "tree_map_only",
    "tree_map_only_",
    "tree_all",
    "tree_any",
    "tree_all_only",
    "tree_any_only",
    "_broadcast_to_and_flatten",
    "treespec_dumps",
    "treespec_loads",
    "treespec_pprint",
]

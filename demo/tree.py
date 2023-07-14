
# Tree:
#       A tree has a root label and a sequence of branches. 
#       Each branch of a tree is a tree. A tree with no branches is called a leaf.
#       Any tree contained within a tree is called a sub-tree of that tree (such as a branch of a branch).
#       The root of each sub-tree of a tree is called a node in that tree.


# The data abstraction for a tree consists of the constructor tree and the selectors label and branches.

def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    """ The is_tree function is applied in the tree constructor to verify that all branches are well-formed. """
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """ The is_leaf function checks whether or not a tree has branches. """
    return not branches(tree)

def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])
# >>> print(fib_tree(3))
# [2, [1], [1, [0], [1]]]

def count_leaves(tree):
    """ The count_leaves function counts the leaves of a tree. """
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)
# >>> print(count_leaves(fib_tree(3)))
# 3

# A partition tree for n using parts up to size m is a binary (two branch) tree that represents the choices taken during computation.
# In a non-leaf partition tree:
#   - the left (index 0) branch contains all ways of partitioning n using at least one m,
#   - the right (index 1) branch contains partitions using parts up to m-1, and
#   - the root label is m.
# The labels at the leaves of a partition tree express whether the path from the root of the tree to the leaf represents a successful partition of n.
def partition_tree(n, m):
    """ Return a partition tree of n using parts of up to m. """
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return tree(m, [left, right])
# >>> partition_tree(2, 2)
# [2, [True], [1, [1, [True], [False]], [False]]]

def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if label(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)
# >>> print_parts(partition_tree(2,2))
# 2
# 1 + 1


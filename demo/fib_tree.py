def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = tree(n - 2), tree(n - 1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])

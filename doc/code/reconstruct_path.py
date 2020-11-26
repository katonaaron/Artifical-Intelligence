def reconstructPath(node):
    """
    Reconstructs a path, whose end node is given as a parameter, by iterating through the parent references.

    node: search node, instance of Node
    """

    if not node:
        return None

    path = []
    while node.parent is not None:
        path = path + [node.action]
        node = node.parent
    path.reverse()
    return path
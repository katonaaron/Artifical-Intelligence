def iterativeDeepeningSearch(problem):
    """
    Search the deepest nodes in the search tree first. The search depth is limited, but the limit is increased in each
    iteration.

    returns:
    - node: the goal node containing reference to its parent, or False if no solution was found.
    """

    depth = 0
    while True:
        (result, cutoff) = depthLimitedSearch(problem, depth)
        if not cutoff:
            return reconstructPath(result)
        depth += 1
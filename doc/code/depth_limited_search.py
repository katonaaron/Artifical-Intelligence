def depthLimitedSearch(problem, limit):
    """
    Search the deepest nodes in the search tree first. The search depth is limited by the given parameter.

    returns a (node, cutoff) tuple:
    - node is the goal node containing reference to its parent.
    - cutoff is True if no solution was found in the given limit, False otherwise.
    """

    start_node = Node(problem.getStartState(), None, 0, None)
    visited = {start_node.state}
    return recursiveDLS(problem, visited, start_node, limit)


def recursiveDLS(problem, visited, node, limit):
    """
    Helper function for depthLimitedSearch(problem, limit).

    returns a (node, cutoff) tuple:
    - node: the goal node containing reference to its parent, or False if no solution was found.
    - cutoff: True if no solution was found in the given limit, False otherwise.
    """

    if problem.isGoalState(node.state):
        return node, False
    if limit == 0:
        return None, True

    cutoff_occurred = False
    for child_state, child_action, child_cost in problem.getSuccessors(node.state):
        if child_state not in visited:

            child = Node(child_state, child_action, child_cost, node)

            visited.add(child_state)
            (result, cutoff) = recursiveDLS(problem, visited, child, limit - 1)
            visited.remove(child_state)

            if cutoff:
                cutoff_occurred = True
            elif result:
                return result, False

    if cutoff_occurred:
        return None, True
    else:
        return None, False
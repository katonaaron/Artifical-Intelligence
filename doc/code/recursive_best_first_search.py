def recursiveBestFirstSearch(problem, heuristic=nullHeuristic):
    """
    Similarly to the DFS, search the deepest nodes in the search tree first, but uses the f_limit variable to keep
    track of the f values. The f value is the largest reached g(n) + h(n) value upon one path after the search is
    stopped because of the f_limit. This f values is backed up to the parent of a node upon backtracking. The f_limit of
    the best child path is the f value of the best alternative path.

    returns:
    - node: the goal node containing reference to its parent, or False if no solution was found.
    """
    start_node = Node(problem.getStartState(), None, 0, None)
    start_node.f = 0
    visited = {start_node.state}
    result, _ = RBFS(problem, heuristic, visited, start_node, float('inf'))

    return reconstructPath(result)


def RBFS(problem, heuristic, visited, node, f_limit):
    """
    Helper function of recursiveBestFirstSearch(problem, heuristic).

    returns:
    - node: the goal node containing reference to its parent, or None if no solution was found.
    - f-cost: the f value obtained on the path.
    """

    if problem.isGoalState(node.state):
        return node, None

    successors = util.PriorityQueueWithFunction(lambda n: n.f)

    for child_state, child_action, child_cost in problem.getSuccessors(node.state):
        if child_state not in visited:
            path_cost = child_cost + node.cost
            child_f = max(path_cost + heuristic(child_state, problem), node.f)
            child = Node(child_state, child_action, path_cost, node, child_f)
            successors.push(child)

    if successors.isEmpty():
        return None, float('inf')

    while True:
        best = successors.pop()

        if best.f > f_limit:
            return None, best.f

        if successors.isEmpty():
            alternative_f = float('inf')
        else:
            alternative = successors.pop()
            alternative_f = alternative.f
            successors.push(alternative)

        visited.add(best.state)
        result, best.f = RBFS(problem, heuristic, visited, best, min(f_limit, alternative_f))
        visited.remove(best.state)

        if result:
            return result, best.f

        successors.push(best)
def iterativeDeepeningAStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first. It differs from A* by limiting the size of
    the frontier, using a bound on the f value.
    """

    start = problem.getStartState()
    bound = heuristic(start, problem)
    path = [(start, None, 0)]
    visited = {start}

    while True:
        t = iterativeDeepeningAStarSearchUtil(problem, heuristic, path, visited, bound)

        if t is None:
            return [action for (state, action, cost) in path if action is not None]
        if t == sys.maxint:
            return None

        bound = t


def iterativeDeepeningAStarSearchUtil(problem, heuristic, path, visited, bound):
    """
    Utility function for iterativeDeepeningAStarSearch.
    Returns the  minimum cost of all values that exceeded the current bound.
    """
    state, action, cost = path[-1]
    f = cost + heuristic(state, problem)

    if f > bound:
        return f
    if problem.isGoalState(state):
        return None

    min = sys.maxint

    for child_state, child_action, child_cost in problem.getSuccessors(state):
        if child_state not in visited:
            visited.add(child_state)
            path.append((child_state, child_action, child_cost + cost))

            t = iterativeDeepeningAStarSearchUtil(problem, heuristic, path, visited, bound)

            if t is None:
                return None
            if t < min:
                min = t

            path.pop()
            visited.remove(child_state)

    return min
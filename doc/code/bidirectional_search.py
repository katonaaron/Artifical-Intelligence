def bidirectionalSearch(problem):
    """
    Simultaneously searches from both the start and the goal positions.
    Stops when the two frontiers intersect.
    The shallowest node is taken first (BFS).
    """

    forward = util.Queue()
    start = problem.getStartState()
    exploredForward = {start}
    forward.push((start, []))

    backward = util.Queue()
    goal = problem.goal
    exploredBackward = {goal}
    backward.push((goal, []))

    visitedForward = set()
    visitedBackwards = set()

    while not forward.isEmpty() and not backward.isEmpty():

        # Forward searching
        currentNode, currentActions = forward.pop()

        if currentNode not in visitedForward:
            visitedForward.add(currentNode)
            if currentNode in exploredBackward:
                while not backward.isEmpty():
                    node, actions = backward.pop()
                    if node == currentNode:
                        solution = currentActions + actions.reverse()
                        return solution

            for (childState, childAction, childCost) in problem.getSuccessors(currentNode):
                forward.push((childState, currentActions + [childAction]))
                exploredForward.add(childState)

        # Backward searching
        currentNode, currentActions = backward.pop()

        if currentNode not in visitedBackwards:

            visitedBackwards.add(currentNode)
            if currentNode in exploredForward:

                while not forward.isEmpty():
                    node, actions = forward.pop()
                    if node == currentNode:
                        backwardActions = [reverseAction(action) for action in currentActions]
                        backwardActions.reverse()
                        solution = actions + backwardActions
                        return solution

            for (childState, childAction, childCost) in problem.getSuccessors(currentNode):
                backward.push((childState, currentActions + [childAction]))
                exploredBackward.add(childState)
    return None


def reverseAction(action):
    """Changes the action to its inverse."""

    if action == 'North':
        return 'South'
    elif action == 'South':
        return 'North'
    elif action == 'West':
        return 'East'
    else:
        return 'West' 

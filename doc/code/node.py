class Node:
    """
    Node used for search algorithms.
    """

    def __init__(self, state, action, cost, parent, f=0):
        """
        state: (x,y) coordinates
        action: direction from Directions of game.py
        cost: cost of reaching the node
        parent: parent node
        f: the backed-up f-value
        """
        self.state = state
        self.action = action
        self.cost = cost
        self.parent = parent
        self.f = f
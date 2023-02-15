# Define the Tree class
class Tree:
    # Attribute
    class_var = "Tree Decrement"

    def __init__(self, t, t_from, t_to, val):
        self.t = t
        self.t_from = t_from
        self.t_to = t_to
        self.val = val

    def getDistance(self, x, y):

        # If the given nodes are the same
        if x == y:
            return 0

        children = []
        for i in range(self.t - 1):
            if self.t_from[i] == x:
                children.append(self.t_to[i])
            if self.t_to[i] == x:
                children.append(self.t_from[i])
        dist = self.t
        print(children)
        for child in children:
            dist = min(self.getDistance(child, y), dist)

        return dist + 1


my_tree = Tree(6,
               [1, 1, 2, 2, 3, 6],
               [2, 3, 4, 5, 6, 7],
               [1, 2, 3, 4, 5, 3, 2])
d1 = my_tree.getDistance(1, 7)
print(d1)

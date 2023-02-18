# Define the Tree class
class Tree:
    # Attribute
    class_var = "Tree Decrement"

    def __init__(self, t, t_from, t_to, val):
        self.t = t
        self.t_from = t_from
        self.t_to = t_to
        self.val = val

    def getPath(self, x, y, path = []):

        # If the given nodes are the same
        if x == y:
            print("Reach the destination!")
            return [x]

        negbs = []
        for i in range(self.t - 1):
            if self.t_from[i] == x and self.t_to[i] not in path:
                negbs.append(self.t_to[i])
            if self.t_to[i] == x and self.t_from[i] not in path:
                negbs.append(self.t_from[i])

        path.append(x)
        # print(path)
        if negbs == []:
            return [-1]

        for negb in negbs:
            # print(negb)
            nextPath = self.getPath(negb, y, path)
            if nextPath and y in nextPath:
                print(nextPath)
                return path + nextPath
        print("Cannot reach y!")

        return [-1]

    def treeDecrement(self):
        return 4

###############
#### Test Cases
###############


my_tree0 = Tree(7,
               [1, 1, 2, 2, 3, 6],
               [2, 3, 4, 5, 6, 7],
               [1, 2, 3, 4, 5, 3, 2]
            )
cost0 = 4



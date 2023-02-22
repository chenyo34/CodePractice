# Define the Tree class
class Tree:
    # Attribute
    class_var = "Tree Decrement"

    def __init__(self, t, t_from, t_to, val):
        self.t = t
        self.t_from = t_from
        self.t_to = t_to
        self.val = val

    def showTree(self):
        print("==== t_from =========")
        print(self.t_from)
        print("==== t_to ==========")
        print(self.t_to)
        print("==== val ===========")
        print(self.val)

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



    def min_cost(self):
        t = self.t
        val = self.val
        t_from = self.t_from
        t_to = self.t_to

        for i in range(len(val)):
            val[i] = val[i]%2

        map = [set() for i in range(t)]
        for i in range(len(t_from)):
            map[t_from[i]-1].add(t_to[i]-1)
            map[t_to[i]-1].add(t_from[i]-1)

        childs = [i for i in range(t) if len(map[i]) == 1]
        remaining = t
        cost = 0

        while childs and remaining > 2:
            remaining -= len(childs)
            new_childs = []
            for l in childs:
                parent = map[l].pop()
                map[parent].remove(l)
                if val[l] == 1:
                    cost += 1
                    val[parent] = 1-val[parent]
                if len(map[parent]) == 1:
                    new_childs.append(parent)
            childs = new_childs

        if childs and val[childs[0]] == 1:
            cost += 1
        return cost

    #     cur_child = []
    #     cur = check_list[0]
    #     cur_child = {1: map[cur]}
    #     check_list.remove(cur)
    #     while check_list:
    #         next_child = dict()
    #         for key in cur_child.keys():
    #             for child in cur_child[key]:
    #                 if child in check_list:
    #                     check_list.remove(child)
    #                     cost += key
    #                     next_child[1] = map[child]
    #                 else:
    #                     next_child[key+1] = map[child]
    #         cur_child = next_child

    #     return cost



###############
#### Test Cases
###############


my_tree = Tree(7,
               [1, 1, 2, 2, 3, 6],
               [2, 3, 4, 5, 6, 7],
               [1, 2, 3, 4, 5, 3, 2])


print(my_tree.min_cost())




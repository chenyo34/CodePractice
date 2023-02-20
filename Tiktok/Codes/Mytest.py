######################################
# Please change the second line in the importing, replace it by your package. Feel free to change the name to your
# cost calculated function. If you want to test more cases, you can use the built-in function createValidTree to
# test random valid Trees
######################################


import unittest
from Tree import Tree
import random


def createValidTree(num, step):

    """
    num: positive integer
        The number of nodes you want to generate
    step: positive integer
        The number of times you want to add values
    """

    # Input Assertion
    # assert(num > 0, "The number of nodes should be positive")
    # assert(step > 0, "The number of steps should be positive")

    nodes = []
    t_from = []
    t_to = []
    val = [0] * num

    # Choose the parent randomly for each new coming node
    for i in range(1, num + 1):
        if len(nodes) != 0:
            parent = random.randint(1, len(nodes))
            t_from.append(parent)
            t_to.append(i)
        nodes.append(i)

    # Randomly choose two exiting nodes and add 1 to there value
    while step > 0:
        x = random.randint(1, num)
        y = random.randint(1, num)
        val[x - 1] += 1
        val[y - 1] += 1
        step -= 1

    return Tree(num,t_from, t_to,val), t_from, t_to, val


class MyTestCase(unittest.TestCase):

    # def test_random(self):
    #     rd_t_from, rd_t_to, rd_val = createValidTree(5, 3)
    #     print(5,
    #           rd_t_from,
    #           rd_t_to,
    #           rd_val)

    def testcase0(self):
        testTree0 = Tree(1,
                         [],
                         [],
                         [100])
        self.assertEqual(testTree0.min_cost(), 0)

    def testcase1(self):
        testTree1 = Tree(7,
                         [1, 1, 2, 2, 3, 6],
                         [2, 3, 4, 5, 6, 7],
                         [1, 2, 3, 4, 5, 3, 2]
                         )
        self.assertEqual(testTree1.min_cost(), 4)

    def testcase2(self):
        testTree2 = Tree(7,
                         [1, 2, 3, 4, 5, 7],
                         [2, 3, 4, 5, 6, 6],
                         [7, 6, 5, 4, 3, 2, 1]
                         )
        self.assertEqual(testTree2.min_cost(), 4)

    def testcase3(self):
        testTree3 = Tree(5,
                         [1, 2, 1, 1],
                         [2, 3, 4, 5],
                         [3, 0, 1, 1, 1]
                         )
        self.assertEqual(testTree3.min_cost(), 4)

    def testRandomCases(self):
        randomtree = createValidTree(5,5)[0]
        randomtree.showTree()

        print("=============================")
        # Calculate the min cost for it
        print(randomtree.min_cost())

if __name__ == '__main__':
    unittest.main()

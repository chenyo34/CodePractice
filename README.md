# CodePractice

Code Interview Questions Implementation

## Question1 --- Tree Decrement

Please see the latest version by the following shared Notion link.  
https://www.notion.so/Tree-Decrement-e84e1514b19f4f819ff1916ee89a9ed1?pvs=4

*Tree Decreasment*

A tree can be represented as an unweighted undirected graph of $t$ nodes nodes numbered from $1$ to $t$ nodes and $t-1$  edges where the $i^{th}$ edge connects the nodes numbered t_from $[i]$ and t_to $[i]$.

A value $\text{val}[i]$ is associated with $i^{th}$ node. In a single operation, two nodes *(could be the same node)* can be selected, and their(its) value(s) can be decremented by 1 at a cost equal to the distance between the two nodes, i.e, the number of edges in the simple path between them. The distance between it and itself is 0.

Given the tree, $t$, and the values $\text{val}$, find the minimum cost to decrease the values of all the nodes to 0. It is guaranteed that the values of all the nodes can be decreased to exactly 0.

**Example**  
Suppose $t$ = 3, t_from = [1, 1],  t_to = [2, 3] and $\text{val} = [3, 1, 2]$.The optimal strategy is to choose nodes 1 and 2 at cost 1. The values become [2, 0, 2]. Now nodes 1 and 1, followed by 3 and 3, can be chosen, each with a cost of 0. Thus the total cost is 1 + 0 + 0 = 1.

**Possible Solution**:

To minimize the cost, we'd like to see the **best secriano** (all nodes have a even value, which implies that they can complete the decreasement with 0 cost in total).

Also, since the question gurantees that the given tree can be decreased to 0, which means there must be a "true" pair for each node 

$$
V = \\{1, \dots, t\\},
E = \\{e_1, \dots, e_{t-1}\\},
P=\\{(x_1,y_1), \dots, (x_n, y_n)\\}\ \text{where } x_i, y_i \in V,
$$

## Question 2 -- Multi-dimensional Selection

Given a 2-d array arr of size n x m, a selection is defined as an array of integers such that it contains ateast ( m/ 21 integers from each row of arr. The cost of the selection is defined as the maximumdifference between any two integers of the selection.
Suppose kis the minimum cost of all the possible selections for the given 2-d array. Find themaximum value of the product of k* the number of integers considered in the selection with theminimum cost.  

**Example** 

Suppose n = 3, m = 2, and arr = [[1, 2], [3, 4], [8, 9]]
Some of the possible selections are [2, 3, 8], [1, 2, 3, 9], [1, 3, 4, 8, 9] etc. The cost of these selectionsare 8 - 2 = 6, 9 - 1 = 8, and 8 respectively.
Here the minimum cost of all the possible selections is 6. The possible selections with the cost 6 are2, 4, 8] and [2, 3, 4, 8]. The maximum value of the required product is obtained using the latterselection i.e.6*4 = 24. Hence the answer is 24.
Function DescriptionComplete the function getMaxProductin the editor below.
getMaxProduct has the following parameter:int arrln][m]: the given 2-d array
Returns
int: the maximum possible product

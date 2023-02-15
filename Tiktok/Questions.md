*Tree Decreasment*

A tree can be represented as an unweighted undirected graph of $t$ nodes nodes numbered from $1$ to $t$ nodes and $t-1$  edges where the $i^{th}$ edge connects the nodes numbered t_from$[i]$ and t\_to$[i]$.  


A value $\text{val}[i]$ is associated with $i^{th}$ node. In a single operation, two nodes *(could be the same node)* can be selected, and their(its) value(s) can be decremented by 1 at a cost equal to the distance between the two nodes, i.e, the number of edges in the simple path between them. The distance between it and itself is 0.  


Given the tree, $t$, and the values $\text{val}$, find the minimum cost to decrease the values of all the nodes to 0. It is guaranteed that the values of all the nodes can be decreased to exactly 0.  


**Example**  
Suppose $t$ = 3, $\text{t\_from} = [1, 1]$,  $\text{t\_to} = [2, 3]$ and $\text{val} = [3, 1, 2]$.The optimal strategy is to choose nodes 1 and 2 at cost 1. The values become [2, 0, 2]. Now nodes 1 and 1, followed by 3 and 3, can be chosen, each with a cost of 0. Thus the total cost is 1 + 0 + 0 = 1.

Possible Solution:

To minimize the cost, we'd like to see the best secriano (all nodes have a even value, which implies that they can complete the decreasement with 0 cost in total).     

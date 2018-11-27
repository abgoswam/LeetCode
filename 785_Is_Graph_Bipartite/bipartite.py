#Uses python3

import sys
import queue


# return 1 if looks good for connected component, else 0
def dfs(adj, v, indicator, ind):
    indicator[v] = ind

    neighbors = adj[v]
    for neigh in neighbors:
        neigh_ind = indicator[neigh]
        if neigh_ind == -1:
            # new node, need to visit
            ret = dfs(adj, neigh, indicator, 1 - ind)
            if not ret:
                return False
        else:
            # neighbor node visited previously, just make sure its different color
            if neigh_ind == ind:
                return False

    return True


class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        # write your code here
        # print(adj)

        n = len(graph)
        indicator = [-1 for _ in range(n)]

        for v in range(n):
            if indicator[v] == -1:
                ret = dfs(graph, v, indicator, 0)
                if not ret:
                    return False

        return True


if __name__ == '__main__':
    s = Solution()

    print(s.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
    print(s.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))

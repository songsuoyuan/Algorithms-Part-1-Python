# Weighted quick-union (with path compression)
# Support union and find operations in log(N) time.

class weightedUnionFind:
    # initialize an empty union-find class with N components
    # from 0 to N-1
    def __init__(self, N):
        self.N = N
        self.count = N
        self.parent = [i for i in xrange(N)]
        self.size = [1 for i in xrange(N)]

    def count(self):
        """
        @return the number of components
        """
        return count;

    def findRoot(self, p):
        """
        return the root of component containing site p.
        @param p the integer representing one site
        @return the root of this component
        """
        assert p >=0 and p < self.count
        rootP = p
        # find root
        while rootP != self.parent[rootP]:
            rootP = self.parent[rootP]
        # path compression
        while p != self.parent[p]:
            pSave = p
            p = self.parent[p]
            self.parent[pSave] = rootP
        return p

    def isConnected(self, p, q):
        """
        Are two sites p and q in same component?
        @param p the integer representing one site
        @param q the integer representing the other site
        @return True if the two sites in the same component
        """
        return self.findRoot(p) == self.findRoot(q)

    def union(self, p, q):
        """
        Merge the component comtaining p and the other component q.
        @param p the integer representing one site
        @param q the integer representing the other site
        @return None
        """
        rootP = self.findRoot(p)
        rootQ = self.findRoot(q)
        if self.size[rootP] < self.size[rootQ]:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        else:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        self.count -=1

if __name__ == '__main__':
    uf = weightedUnionFind(13)
    uf.parent = [0, 0, 0, 1, 1, 1, 3, 3, 6, 6, 8, 9, 9]
    print('id:')
    print(uf.parent)
    print('Are site 8 and site 9 connected?')
    print(uf.isConnected(8,9))
    print('Now id becomes:')
    print(uf.parent)

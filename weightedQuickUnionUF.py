# Weighted quick-union (with path compression)
# Support union and find operations in log(N) time.
# 
# Test example:
# user$ python weightedQuickUnionUF.py tinyUF.txt
# 2 components

class weightedQuickUnionUF:
    # initialize an empty quick union class with N components
    # from 0 to N-1
    def __init__(self, N):
        self._N = N
        self._count = N
        self._parent = [i for i in xrange(N)]
        self._size = [1 for i in xrange(N)]

    def components(self):
        """
        @return the number of components
        """
        return self._count

    def findRoot(self, p):
        """
        return the root of component containing site p.
        @param p the integer representing one site
        @return the root of this component
        """
        assert p >=0 and p < self._N
        rootP = p
        # find root
        while rootP != self._parent[rootP]:
            rootP = self._parent[rootP]
        # path compression
        while p != self._parent[p]:
            pSave = p
            p = self._parent[p]
            self._parent[pSave] = rootP
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
        if self._size[rootP] < self._size[rootQ]:
            self._parent[rootP] = rootQ
            self._size[rootQ] += self._size[rootP]
        else:
            self._parent[rootQ] = rootP
            self._size[rootP] += self._size[rootQ]
        self._count -= 1

if __name__ == '__main__':
    import sys
    import os.path
    if len(sys.argv) > 1:
        baseDir = os.path.join('Data')
        fileNane = os.path.join(baseDir, sys.argv[1])
        if os.path.isfile(fileNane):
            f = open(fileNane, 'r')
            N = int(f.readline())
            uf = weightedQuickUnionUF(N)
            for line in f.readlines():
                x, y = [int(t) for t in line[:-1].split(' ')]
                if uf.isConnected(x, y):
                    continue
                uf.union(x, y)
            print uf.components(), 'components'
        else:
            print 'File not exists, possible solution:' 
            print 'Use python weightedQuickUnionUF.py tinyUF.txt '\
                'instead of \\Data\\tinyUF.txt'
    else:
        print 'No file name given, program exit.'

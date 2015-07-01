# Stack implementation with resizing arrays
# Double when stack is full, halve when stack is one-quarter full
#
# Test example:
# user$ more tobe.txt
# to be or not to - be - - that - - - is
# user$ python arrayStack.py tobe.txt
# to be not that or be

class arrayStack:
    # initialize an empty stack with fixed size 2
    def __init__(self):
        self._a = [None, None]
        self._N = 0

    # implement class iterable
    def __iter__(self):
        return iter(self._a[self._N-1::-1])

    # is stack empty?
    def isEmpty(self):
        return self._N == 0

    # resize the list while hoding the elements
    def _resize(self, cap):
        temp = cap * [None]
        temp[:self._N] = self._a[:self._N]
        self._a = temp

    # push an item into stack 
    def push(self, item):
        if self._N == len(self._a):
            self._resize(2 * len(self._a))
        self._a[self._N] = item
        self._N += 1

    # delete and return the item on the top of stack
    def pop(self):
        if self.isEmpty():
            raise IndexError('Stack underflow.')
        self._N -= 1
        item = self._a[self._N]
        self._a[self._N] = None    # avoid loitering
        if self._N > 0 and self._N == len(self._a) / 4:
            self._resize(len(self._a) / 2)
        return item

if __name__ == '__main__':
    import sys
    import os.path
    if len(sys.argv) > 1:
        baseDir = os.path.join('Data')
        fileNane = os.path.join(baseDir, sys.argv[1])
        if os.path.isfile(fileNane):
            f = open(fileNane, 'r')
            s = f.read()[:-1]
            stack = arrayStack()
            for item in s.split():
                if item != '-':
                    stack.push(item)
                elif stack.isEmpty():
                    print 'Empty stack.'
                    sys.exit('Bad Input in ' + fileNane)
                else:
                    print stack.pop(),
        else:
            print 'File not exists, possible solution:' 
            print 'Use python arrayStack.py tobe.txt '\
                'instead of \\Data\\tobe.txt'
    else:
        print 'No file name given, program exit.'

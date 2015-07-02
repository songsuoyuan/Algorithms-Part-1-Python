# Queue implementation with resizing arrays (iterable)
# Double when queue is full, halve when queue is one-quarter full
#
# Methods:
# boolean   isEmpty()
# int       count()
# None      enqueue()
# item      dequeue()
# item      first()
#
# Test example:
# user$ more tobe.txt
# to be or not to - be - - that - - - is
# user$ python arrayQueue.py tobe.txt
# to be or not to be (2 left in queue)

class arrayQueue:
    # initialize an empty queue with fixed size 2
    def __init__(self):
        self._a = [None, None]
        self._N = 0
        self._first = 0
        self._last = 0

    # implement class iterable
    def __iter__(self):
        if self._last > self._first:
            return iter(self._a[self._first:self._last])
        else:
            return iter(self._a[self._first:] + 
                        self._a[:self._last])

    # is queue empty?
    def isEmpty(self):
        return self._N == 0

    # return queue size
    def count(self):
        return self._N

    # resize the list while hoding the elements
    def _resize(self, cap):
        assert cap >= self._N
        temp = cap * [None]
        if self._last > self._first:
            temp[:self._N] = self._a[self._first:self._last]
        else:
            temp[:self._N] = (self._a[self._first:] + 
                              self._a[:self._last])
        self._a = temp
        self._first = 0
        self._last = self._N

    # add an item to the last of queue
    def enqueue(self, item):
        if self._N == len(self._a):
            self._resize(2 * len(self._a))
        self._a[self._last] = item
        self._last += 1
        if self._last == len(self._a):
            self._last = 0
        self._N += 1

    # delete and return the item at the first of queue
    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Queue underflow.')
        item = self._a[self._first]
        self._a[self._first] = None # avoid loitering
        self._N -= 1
        self._first += 1
        if self._first == len(self._a):
            self._first = 0
        if self._N > 0 and self._N == len(self._a) / 4:
            self._resize(len(self._a) / 2)
        return item

    # return the first item in queue
    def first(self):
        if self.isEmpty():
            raise IndexError('Queue underflow.')
        return self._a[self._first]

if __name__ == '__main__':
    import sys
    import os.path
    if len(sys.argv) > 1:
        baseDir = os.path.join('Data')
        fileNane = os.path.join(baseDir, sys.argv[1])
        if os.path.isfile(fileNane):
            f = open(fileNane, 'r')
            s = f.read()[:-1]
            queue = arrayQueue()
            for item in s.split():
                if item != '-':
                    queue.enqueue(item)
                elif queue.isEmpty():
                    print 'Empty queue.'
                    sys.exit('Bad Input in ' + fileNane)
                else:
                    print queue.dequeue(),
            print '\n', queue.count(), 'left in stack:'
            for item in queue:
                print item,
        else:
            print 'File not exists, possible solution:' 
            print 'Use python arrayStack.py tobe.txt '\
                'instead of \\Data\\tobe.txt'
    else:
        print 'No file name given, program exit.'

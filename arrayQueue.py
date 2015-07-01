# Queue implementation with resizing arrays
# Double when queue is full, halve when queue is one-quarter full
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
        if self._last >= self._first:
            return iter(self._a[self._first:self._last + 1])
        else:
            return iter(self._a[self._first:] + 
                        self._a[:self._last + 1])

    # is queue empty?
    def isEmpty(self):
        return self_N == 0

    
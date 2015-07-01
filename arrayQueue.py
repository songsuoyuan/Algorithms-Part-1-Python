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
    def __init__(self, N):
        self._a = [None, None]
        self._N = 0
        self._first = 0
        self._last = 0

    def __iter__()

    # is queue empty?
    def isEmpty(self):
        return self_N == 0


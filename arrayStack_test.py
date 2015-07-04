#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Unit test for arrayStack:
#
# init:     class method
# test_1:   randomly push, pop and count
# test_2:   pop from empty stack

import random
import unittest
from arrayStack import arrayStack
from collections import deque

class TestStack(unittest.TestCase):
    def test_init(self):
        stack = arrayStack();
        attr = ['isEmpty', 'count', 'push', 'pop', 'top']
        for a in attr:
            self.assertTrue(hasattr(stack, a))

    def test_1(self):
        """ Call push(), pop() and count() with probability 
        p1, p2 and p3.
        """
        dq = deque()
        stack = arrayStack();
        p1, p2, p3 = (0.4, 0.4, 0.2)
        count = 0
        stackSize = 0
        calls = 1000
        while (count < calls):
            r = random.uniform(0,1)
            if r < p1:
                dq.append(r)
                stack.push(r)
                count += 1
                stackSize += 1
            elif r < p1 + p2:
                if stackSize == 0:
                    continue
                self.assertEqual(dq.pop(), stack.pop())
                count += 1
                stackSize -= 1
            else:
                self.assertEqual(stackSize, stack.count())

    def test_2(self):
        """ Pop from an empty stack
        """
        stack = arrayStack()
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.top()
        count = 0
        calls = 1000
        while count < calls:
            procedure = [1,0] * 10
            random.shuffle(procedure)
            procedure = [1] + procedure + [0, 0]
            with self.assertRaises(IndexError):
                for p in procedure:
                    if p == 1:
                        stack.push(p)
                    else:
                        stack.pop()
            count += 1

if __name__ == '__main__':
    unittest.main()
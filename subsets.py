#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Subset take an integer k and a sequence of N objects as input,
# and subset return exactly k of N objects uniformly at random.
# The probability of returning a particular object is k / N.

class subset:
    # initialize a subset class with iterable object representing 
    # N objects as input.
    def __init__(self, k, iterableList):
        
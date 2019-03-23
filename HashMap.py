#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 10:50:18 2018

@author: Arut
"""

from collections import MutableMapping
from random import randrange


class MapBase(MutableMapping):
    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self._key < other._key


class HashMapBase(MapBase):
    def __init__(self, N=11, p=109345121):
        self._N = N  # capacity
        self._table = N * [None]
        self._n = 0  # actual size
        self._p = p
        self._a = 1 + randrange(p - 1)
        self._b = randrange(p)

    def _hash_function(self, k):
        i = hash(k)  # hash code
        # MAD : ((ai + b) % p ) % N
        return ((self._a * i + self._b) % self._p) % self._N

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        # find the hash value
        hash_value = self._hash_function(k)
        # return self._table[hash_value]
        return self._getbucket_item(hash_value, k)

    def __setitem__(self, k, v):
        # find the hash value
        hash_value = self._hash_function(k)
        # self._table[hash_value] = Item(k,v)
        self._setbucket_item(hash_value, k, v)

    def __delitem__(self, k):
        # find the hash value
        hash_value = self._hash_function(k)
        # self._table[hash_value] = None
        self._delbucket_item(hash_value, k)


class ChainHashMap(HashMapBase):
    def _getbucket_item(self, hash_value, k):
        # bucket is a list
        bucket = self._table[hash_value]
        if bucket:
            # search for k
            for item in bucket:
                if item._key == k:
                    return item._value
            raise KeyError('Key not found')
        else:
            raise KeyError('Key not found')

    def _setbucket_item(self, hash_value, k, v):
        if self._table[hash_value] == None:
            self._table[hash_value] = []

        # search for the key k
        bucket = self._table[hash_value]
        index = -1
        for index in range(len(bucket)):
            if bucket[index]._key == k:
                bucket[index]._value = v

        if index < 0:
            # insert new item
            new_item = ChainHashMap._Item(k, v)
            bucket.append(new_item)
            self._n += 1

    def _delbucket_item(self, hash_value, k):
        # search for the key k
        bucket = self._table[hash_value]
        if bucket == None:
            raise KeyError('Key not found')
        index = -1
        for index in range(len(bucket)):
            if bucket[index]._key == k:
                break

        if index < 0:
            raise KeyError('Key not found')
        else:
            item = bucket[index]
            bucket.remove(item)
            self._n -= 1

    def __iter__(self):
        for bucket in self._table:
            if bucket != None:
                for item in bucket:
                    yield item._key


class LinearProbeHashMap(HashMapBase):
    # refactor the code
    def _find_slot(self, hash_value, k):
        index = hash_value
        if self._table[index] is None \
                or self._table[index]._key == k:
            return index
        else:
            index = (index + 1) % self._N
            while self._table[index] != None \
                    and self._table[index]._key != k:
                index = (index + 1) % self._N
            return index

    def _getbucket_item(self, hash_value, k):
        index = self._find_slot(hash_value, k)
        if self._table[index] is None:
            raise KeyError('Key not found')
        else:
            return self._table[index]._value

    def _setbucket_item(self, hash_value, k, v):
        index = self._find_slot(hash_value, k)
        if self._table[index] is None:
            self._table[index] = LinearProbeHashMap._Item(k, v)
            self._n += 1
        else:
            # update value
            self._table[index]._value = v

    # buggy version!!!_
    def _delbucket_item(self, hash_value, k):
        index = self._find_slot(hash_value, k)
        if self._table[index] is None:
            raise KeyError('Key not found')
        else:
            # delete
            del_index = index
            self._table[del_index] = None
            # shift elements
            index = (index + 1) % self._N
            item = self._table[index]
            while item != None and self._hash_function(item._key) > del_index:
                self._table[del_index] = self._table[index]
                index = (index + 1) % self._N
                item = self._table[index]
            self._n -= 1

    def __iter__(self):
        for item in self._table:
            if item != None:
                yield item._key




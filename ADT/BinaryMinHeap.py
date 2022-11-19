import math
from typing import Generic

from ADT.Heap import Heap, T


class BinaryMinHeap(Heap, Generic[T]):

    def min(self):
        return self.head()

    def extract_min(self) -> T:
        if len(self.arr) == 0:
            return None
        if len(self.arr) == 1:
            return self.arr.pop(0)

        val = self.arr[0]
        self.arr[0] = self.arr[len(self.arr) -1]
        self.arr.pop(len(self.arr)-1)
        self.bubble_down(0)
        return val

    def search(self, x: T) -> int | None:
        for i, check in enumerate(self.arr):
            if check == x:
                return i

        return None

    def reorg(self, x: T) -> int:
        i = self.search(x)

        if i is None:
            return None

        return self.bubble_up(i)

    def insert(self, val: T):

        if len(self.arr) == 0:
            self.arr.append(val)
            return 0
        if len(self.arr) == 1:
            self.arr.append(val)
            return 1

        self.arr.append(val)

        i = len(self.arr) - 1

        p_i = self.parent(i)

        while p_i is not None and val < self.arr[p_i]:
            p_val = self.arr[p_i]
            self.arr[p_i] = val
            self.arr[i] = p_val
            i = self.parent(i)
            p_i = self.parent(i)

        return i

    def height(self):
        return math.log(len(self.arr), 2)

    def bubble_down(self, i=0):

        bub = self.arr[i]

        left_i = self.left(i)
        right_i = self.right(i)

        while left_i is not None or right_i is not None:
            if left_i is not None and bub > self.arr[left_i]:
                left = self.arr[left_i]
                self.arr[i] = left
                self.arr[left_i] = bub
                i = left_i
                left_i = self.left(i)
                right_i = self.right(i)
                continue

            if right_i is not None and bub > self.arr[right_i]:
                right = self.arr[right_i]
                self.arr[i] = right
                self.arr[right_i] = bub
                i = right_i
                left_i = self.left(i)
                right_i = self.right(i)
                continue

            break
        return i

    def bubble_up(self, i):
        bub = self.arr[i]
        p_i = self.parent(i)

        while p_i is not None and self.arr[p_i] > bub:
            parent = self.arr[p_i]
            self.arr[i] =parent
            self.arr[p_i] = bub

        return i

    def __len__(self):
        return len(self.arr)
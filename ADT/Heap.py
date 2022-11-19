import math
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')


class Heap(ABC, Generic[T]):

    arr: list[T]

    def __init__(self):
        self.arr = []

    def head(self) -> T:
        if len(self.arr) > 0:
            return self.arr[0]
        return None

    def parent(self, i: int):
        parent = (i-1)//2
        if 0 <= parent < len(self.arr):
            return parent
        return None

    def left(self, i):
        left = 2*i+1
        if 0<=left < len(self.arr):
            return left
        return None

    def right(self, i):
        right = 2*i+2

        if 0 <= right < len(self.arr):
            return right
        return None

    @abstractmethod
    def height(self):
        pass

    @abstractmethod
    def insert(self, val: T):
        pass

    @abstractmethod
    def bubble_down(self, i):
        pass

    @abstractmethod
    def bubble_up(self, i):
        pass

    @abstractmethod
    def search(self, val: T) -> int | None:
        pass


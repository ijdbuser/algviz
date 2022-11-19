from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

T = TypeVar('T')


class TreeNode(ABC, Generic[T]):
    branching_factor: int
    val: T

    def __init__(self, val: T):
        self.val = val


class Tree (ABC):
    head = TreeNode
    depth: int

    def __init__(self):
        self.depth = 0
        self.head = None

    @abstractmethod
    def insert(self, val: T):
        pass

    @abstractmethod
    def delete(self, val: T):
        pass

    @abstractmethod
    def search(self, val: T):
        pass
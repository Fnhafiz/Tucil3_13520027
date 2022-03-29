import copy
from heapq import heappush, heappop

from numpy import true_divide

class PriorityQueue :
    def __init__(self):
        self.heap = []

    def push(self, num):
        heappush(self, num)

    def pop(self, num):
        heappop(self,num)

    def isEmpty(self):
        if not self.heap:
            return True
        else :
            return False

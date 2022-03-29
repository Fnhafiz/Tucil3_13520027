import copy
from heapq import heappush, heappop

from numpy import true_divide

class PriorityQueue :
    # Konstruktor : Inisialisasi Priority Queue
    def __init__(self):
        self.heap = []

    # Melakukan Push : Menambahkan elemen num ke PQ 
    def push(self, num):
        heappush(self.heap, num)

    # Melakukan Pop : Menghapus elemen pertama dari PQ
    def pop(self):
        heappop(self.heap)

    # Mengecek isEmpty : bernilai true jika kosong, false jika sebaliknya
    def isEmpty(self):
        if not self.heap:
            return True
        else :
            return False

class Node :
    def __init__(self, parent, matrix, empty_tile, cost, level):
        self.parent = parent

        self.matrix = matrix

        self.empty_tile = empty_tile

        self.cost = cost

        self.level = level

    def __lt__ (self, next):
        self.cost < next.cost

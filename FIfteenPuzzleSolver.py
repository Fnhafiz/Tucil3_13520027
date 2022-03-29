import copy
from heapq import heappush, heappop
from itertools import count

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

# Menghitung banyaknya jumlah ubin tidak kosong yang tidak terdapat pada susunan akhir
def countCost (initial_matrix, final_matrix) -> int :
    count = 0
    for i in range(4):
        for j in range(4):
            if ((initial_matrix[i][j]) and (initial_matrix[i][j] != final_matrix[i][j])):
                count += 1

    return count

def newNode (parent, matrix, empty_tile, new_empty_tile, level, final_matrix):
    # Menyalin matrix awal ke matrix baru
    new_matrix = copy.deepcopy(matrix)

    x1 = empty_tile[0]
    y1 = empty_tile[1]
    x2 = new_empty_tile[0]
    y2 = new_empty_tile[1]

    # Menukar antara empty_tile dan new_empty_tile setelah melakukan pergerakan
    new_matrix[x1][y1], new_matrix[x2][y2] =  new_matrix[x2][y2], new_matrix[x1][y1]

    # Menghitung banyaknya jumlah ubin yang berbeda dengan susunan akhir
    cost = countCost(new_matrix, final_matrix)

    return node(parent, new_matrix, new_empty_tile, cost, level)






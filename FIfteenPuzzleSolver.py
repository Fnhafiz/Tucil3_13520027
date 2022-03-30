import copy
from heapq import heappush, heappop

class PriorityQueue :
    # Konstruktor : Inisialisasi Priority Queue
    def __init__(self):
        self.heap = []

    # Melakukan Push : Menambahkan elemen num ke PQ 
    def push(self, num):
        heappush(self.heap, num)

    # Melakukan Pop : Menghapus elemen pertama dari PQ
    def pop(self):
        return heappop(self.heap)

    # Mengecek isEmpty : bernilai true jika kosong, false jika sebaliknya
    def isEmpty(self):
        if not self.heap:
            return True
        else :
            return False

class node :
    def __init__(self, parent, matrix, empty_tile, cost, level):
        self.parent = parent

        self.matrix = matrix

        self.empty_tile = empty_tile

        self.cost = cost

        self.level = level

    def __lt__ (self, next):
        return self.cost < next.cost

# bottom, left, top, right
rows = [ 1, 0, -1, 0 ]
cols = [ 0, -1, 0, 1 ]

# Menghitung banyaknya jumlah ubin tidak kosong yang tidak terdapat pada susunan akhir
def countCost (initial_matrix, final_matrix) -> int :
    count = 0
    for i in range(4):
        for j in range(4):
            if ((initial_matrix[i][j]) and (initial_matrix[i][j] != final_matrix[i][j])):
                count += 1

    return count

def newNode (parent, matrix, empty_tile, new_empty_tile, level, final_matrix) -> node:
    # Menyalin matrix awal ke matrix baru
    new_matrix = copy.deepcopy(matrix)

    x1 = empty_tile[0]
    y1 = empty_tile[1]
    x2 = new_empty_tile[0]
    y2 = new_empty_tile[1]

    # Menukar antara empty_tile dan new_empty_tile setelah melakukan pergerakan
    new_matrix[x1][y1], new_matrix[x2][y2] =  new_matrix[x2][y2], new_matrix[x1][y1]

    # Menghitung banyaknya jumlah ubin yang berbeda dengan susunan akhir
    new_cost = countCost(new_matrix, final_matrix)

    new_node = node(parent, new_matrix, new_empty_tile, new_cost, level)
    return new_node


# Mengecek apakah indeks x dan y valid pada matriks
def isValid (x,y):
    return x>=0 and x<4 and y>=0 and y<4


# Menyelesaikan 15-Puzzle
def Solve(initial_matrix, empty_tile, final_matrix):
    
    # Inisialisasi Priority Queue
    pq = PriorityQueue()

    # Menghitung banyaknya jumlah ubin yang berbeda dengan susunan akhir
    current_cost = countCost(initial_matrix, final_matrix)

    # Membuat node baru berupa root dari node awal
    root_node = node(None, initial_matrix, empty_tile, current_cost, 0)

    # Melakukan push root_node sebelumnya ke dalam Priority Queue
    pq.push(root_node)

    while not pq.isEmpty(): 
        min_node = pq.pop()

        # Jika cost = 0, artiny tidak ada lagi ubin yang berbeda dengan susunan akhir
        if min_node.cost == 0 :
            printPath(min_node)
            return
        
        for i in range(4):
            new_tile = [min_node.empty_tile[0] + rows[i],
                        min_node.empty_tile[1] + cols[i],]
            
            if (isValid(new_tile[0], new_tile[1])):
                child = newNode(min_node, min_node.matrix, min_node.empty_tile, new_tile, min_node.level + 1, final_matrix)
                pq.push(child)
                # printMatrix(min_node.matrix)
                # printMatrix(child.matrix)


def printMatrix(mat):
     
    for i in range(4):
        for j in range(4):
            if (mat[i][j] > 0 and mat[i][j] <= 9) :
                print("%d " % (mat[i][j]) + " ", end = " ")   
            elif (mat[i][j] == 16) :
                  print("-  ", end = " ")   
            else :       
                print("%d " % (mat[i][j]), end = " ")     
        print()

def printPath(root_node):
     
    if root_node == None:
        return
     
    printPath(root_node.parent)
    printMatrix(root_node.matrix)
    print()

def isReachable (initial_matrix, empty_tile) -> bool :
    countX = 0
    countLess = 0
    for i in range(4):
        for j in range(4):
            m = i
            n = j
            if(m==i):
                while(n<4):
                    if(initial_matrix[m][n]<initial_matrix[i][j]):
                        countLess += 1
                    n+=1
                m+=1
            while(m<4):
                n = 0
                while(n<4):
                    if(initial_matrix[m][n]<initial_matrix[i][j]):
                        countLess += 1
                    n+=1
                m+=1
    if ((empty_tile[0]+empty_tile[1]) %2 == 1):
        countX += 1
    print("CountX = ", countX)
    print("CountLess = ", countLess)
    countTotal = countX + countLess
    if (countTotal % 2 == 0):
        return True
    else : 
        return False

initial_matrix = [ [ 1, 2, 3, 4 ],
                   [ 5, 6, 16, 8 ],
                   [ 9, 10, 7, 11 ],
                   [ 13, 14, 15, 12 ] ]

initial_matrix_2 = [ [ 1, 3, 4, 15 ],
                   [ 2, 16, 5, 12 ],
                   [ 7, 6, 11, 14 ],
                   [ 8, 9, 10, 13 ] ]

final_matrix = [ [ 1, 2, 3, 4 ],
                 [ 5, 6, 7, 8 ],
                 [ 9, 10, 11, 12 ],
                 [ 13, 14, 15, 16 ] ]

empty_tile = [ 1, 2 ]

empty_tile_2 = [ 1, 1 ]

Solve(initial_matrix, empty_tile, final_matrix)
# isReachable(initial_matrix_2, empty_tile_2)




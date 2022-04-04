import copy
import numpy as np
import time
from tkinter import *
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

# Bergerak ke bawah, kiri, atas, kanan
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
    visited_node = []
    visited_node.append(root_node)

    while not pq.isEmpty(): 
        is_visited = False
        min_node = pq.pop()

        # Jika cost = 0, artiny tidak ada lagi ubin yang berbeda dengan susunan akhir
        if min_node.cost == 0 :
            print("Jumlah simpul yang dibangkitkan = ", min_node.level+1, "\n")
            return min_node

        for i in range(4):
            new_tile = [min_node.empty_tile[0] + rows[i],
                        min_node.empty_tile[1] + cols[i],]
            
            if (isValid(new_tile[0], new_tile[1])):
                child = newNode(min_node, min_node.matrix, min_node.empty_tile, new_tile, min_node.level + 1, final_matrix)
                pq.push(child)

# Mengeluarkan output berupa matriks
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

# Mengeluarkan semua path matriks dari solusi
def printPath(root_node):
     
    if root_node == None:
        return
     
    printPath(root_node.parent)
    printMatrix(root_node.matrix)
    print()

# Mengecek apakah puzzle dapat diselesaikan
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
    print("\nNilai dari fungsi Kurang(i) = ", countLess)
    countTotal = countX + countLess
    print("Nilai dari fungsi Kurang(i) + X = ", countTotal, "\n")
    if (countTotal % 2 == 0):
        return True
    else : 
        return False

# Masukan matriks yang dibangkitkan secara acak
def generate_random():
    initial_matrix = np.arange(1, 17)
    np.random.shuffle(initial_matrix)
    initial_matrix = np.reshape(initial_matrix,(4,4))
    return initial_matrix

# Masukan matriks yang dibangkitkan sesuai input pengguna
def input_user(input):
    with open(input, 'r') as f:
        initial_matrix = [[int(num) for num in line.split(',')] for line in f]
    return initial_matrix

# Mencari letak tile yang kosong (berisi angka 16)
def find_empty_tile(initial_matrix):
    # empty_tile = [ for _ in range(2)]
    empty_tile = [0 for i in range(2)]
    for i in range(4):
        for j in range(4):
            if (initial_matrix[i][j] == 16) :
                empty_tile[0] = i
                empty_tile[1] = j 
                return empty_tile

# GUI Bonus 
# Class Table untuk GUI
class Table:    
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                if(lst[i][j] == 16):               
                    self.e = Entry(root, width=3, fg='white', bg='white',
                                   font=('Arial',16,'bold'))
                    
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j])
                elif(lst[i][j] != 16):
                    self.e = Entry(root, width=3, fg='white', bg='blue',
                                   font=('Arial',16,'bold'))
                    
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j])

# Mengeluarkan output berupa GUI dari solusi
def printPathGUI (root_node):
    global total_rows, total_columns, lst
    if root_node == None:
        return

    printPathGUI(root_node.parent)
    lst = root_node.matrix
    total_rows = len(lst)
    total_columns = len(lst[0])
    root = Tk()
    t = Table(root)
    root.mainloop()

final_matrix = [(1,2,3,4),
                (5,6,7,8),
                (9,10,11,12),
                (13,14,15,16),]


# Main Program
print("________________________________")
print("|        15 Puzzle Solver       |")
print("|_______________________________|")
print("Pilih masukkan yang diinginkan : ")
print("1. Acak ")
print("2. Nama File")

# Memilih ingin masukkan berupa acak atau file
choice = int(input("Masukkan yang diinginkan (Pilih 1/2) = "))
# Jika memilih acak
if (choice == 1):
    initial_matrix = generate_random()
    empty_tile = find_empty_tile(initial_matrix)
    start_time = time.time()
    reach = isReachable(initial_matrix, empty_tile)
    if (reach == False):
        print("Waktu Eksekusi = %s detik\n" % (time.time() - start_time))
        printMatrix(initial_matrix)
        print("\nPersoalan diatas tidak dapat diselesaikan")
    else :
        min_node = Solve(initial_matrix, empty_tile, final_matrix)
        print("Waktu Eksekusi = %s detik\n" % (time.time() - start_time))
        printPath(min_node)
        is_GUI = input("\nApakah ingin menampilkan GUI dari solusi (ya/tidak) = ")
        if (is_GUI == "ya"):
            printPathGUI(min_node)
# Jika memilih nama file
elif (choice == 2):
    file_input = input("Masukkan nama file = ")
    initial_matrix = input_user(file_input)
    empty_tile = find_empty_tile(initial_matrix)
    start_time = time.time()
    reach = isReachable(initial_matrix, empty_tile)
    if (reach == False):
        print("Waktu Eksekusi = %s detik\n" % (time.time() - start_time))
        printMatrix(initial_matrix)
        print("\n Persoalan diatas tidak dapat diselesaikan")
    else :
        min_node = Solve(initial_matrix, empty_tile, final_matrix)
        printPath(min_node)
        print("Waktu Eksekusi = %s detik\n" % (time.time() - start_time))
        is_GUI = input("\nApakah ingin menampilkan GUI dari solusi (ya/tidak) = ")
        if (is_GUI == "ya"):
            printPathGUI(min_node)


else :
    print("Input salah")




import tkinter as tk
from collections import defaultdict
import openpyxl as exel

#ATTENTION: this part is designed by me, but i commented it out becuase i cant use it. its not done yet and it wont be done before the deadline if i use it. Instead im copying one from internet.
# I will switch to my own algorithm back after the deadline!

# class path:
#     paths = {}

#     used = {
#         'A':False,
#         'B':False,
#         'C':False,
#         'D':False,
#         'E':False,
#         'F':False,
#         'G':False,
#         'H':False,
#         'I':False,
#         'J':False
#     }

#     plattegrond = {
#         'A':['C'],
#         'B':['C', 'F'],
#         'C':['A', 'B', 'D'],
#         'D':['C', 'E', 'G', 'I'],
#         'E':['D'],
#         'F':['B'],
#         'G':['D', 'H', 'J'],
#         'H':['G'],
#         'I':['D', 'J'],
#         'J':['G', 'I']
#     }

#     lengths = {
#         'AC':1,
#         'BC':1,
#         'BF':3,
#         'CD':2,
#         'DE':3,
#         'DI':2,
#         'DG':2,
#         'GH':3,
#         'IJ':4,
#         'JG':5,
#         'CA':1,
#         'CB':1,
#         'FB':3,
#         'DC':2,
#         'ED':3,
#         'ID':2,
#         'GD':2,
#         'HG':3,
#         'JI':4,
#         'GJ':5,
#     }

#     class PathToEnd:

#         def __init__(self, path, lengths:list) -> None:
#             self.path = path
#             self.lengths = lengths

#         def getPath(self):
#             return self.path

#         def getTotalLength(self):
#             total = None
#             for length in self.lengths:
#                 total =+ length
#             return total

#     def calclengths(self, path:list):
#         path=[path[i//2] for i in range(len(path)*2)]
#         sidesraw = ''.join(path)
#         sidesraw = sidesraw[1:-1]
#         sides = [sidesraw[i:i+2] for i in range(0, len(sidesraw), 2)]
#         lengths = []
#         for side in sides:
#             lengths.append(self.lengths.get(side))
#         return lengths

#     def resetused(self):
#         self.used = {
#             'A':False,
#             'B':False,
#             'C':False,
#             'D':False,
#             'E':False,
#             'F':False,
#             'G':False,
#             'H':False,
#             'I':False,
#             'J':False
#         }

#     def calcpath(self, Map, lengths, used,currentpath:list, end):
#         temp_used = {
#         'A':False,
#         'B':False,
#         'C':False,
#         'D':False,
#         'E':False,
#         'F':False,
#         'G':False,
#         'H':False,
#         'I':False,
#         'J':False
#     }

#         currentnode = None if len(currentpath) == 0 else currentpath[len(currentpath)-1]
        
#         for NODE in self.plattegrond:
#             if temp_used[NODE]:
#                 adjacent = False
#                 for point in self.plattegrond[NODE]:
#                     adjacent = point == currentnode
#                 if not adjacent:
#                     temp_used.update({NODE:False})

#         if currentpath[len(currentpath)-1] == end:
#             temppath = self.PathToEnd(currentpath, self.calclengths(currentpath))
#             self.paths.update(currentpath, temppath.getTotalLength)

#         for node in self.plattegrond[currentnode]:
#             if not used[node] and not temp_used[node]:
#                 self.calcpath(path, self.lengths, self.used, currentpath+node, end)

#     def calculate(self, Map, start, end):
#         startpath = [start]
#         self.calcpath(path, Map, self.lengths, self.used, startpath, end)
# path.calculate(path,Map=path.plattegrond, start='A',end="B")\

graph1 = {
    'A': ['P'],
    'B': ['P', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'E'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C']
}

Locaties = {
    'Truck':'A',
    'Koelcel':'B',
    'freezer storage':'F',
    'Productie Soft Fried':'C',
    'Weging Soft Fried':'C',
    'Finished':'D',
    'Wrapping':'E',
    'TruckEnd':'G'
}

paden = {
    'AB':['A','P','H','I','B'],
    'BC':['B','I','H','K','N','M','L','C'],
    'DE':['D','H','E'],
    'EF':['E','H','I','J','F'],
    'FG':['F','J','I','H','P','Q','G']
}

padendirect = {
    'AB':['A','P','B'],
    'BC':['B','H','K','N','M','L','C'],
    'DE':['D','H','E'],
    'EF':['E','F'],
    'FG':['F','Q','G']
}

print(padendirect['BC'])

class draw:
    def MainLoop():
        tk.mainloop()
    def main():
        root = tk.Tk()
        root.title("Path layout")
        canvas = tk.Canvas(root, width=1290, height=857)
        canvas.pack()
        circle = lambda x, y, color: canvas.create_oval(20+x, 20+y, 30+x, 30+y, fill=color)
        bg = tk.PhotoImage(file = r"D:\Users\Dennis\Documents\Luc\python 3\Data-points-map\Layout FP plant (1).gif")
        canvas.create_image(0, 0,image=bg, anchor=tk.NW)
        F = circle(300, 450, "lime")
        B = circle(430, 450, 'lime')
        H = circle(540, 480, 'black')
        K = circle(555, 425, 'blue')
        D = circle(520, 430, 'lime')
        N = circle(625, 420, 'blue')
        M = circle(625, 280, 'blue')
        L = circle(900, 270, 'blue')
        C = circle(920, 150, 'lime')
        P = circle(680, 480, 'blue')
        Q = circle(760, 500, 'blue')
        E = circle(630, 510, 'lime')
        A = circle(680, 570, 'lime')
        G = circle(760, 570, 'lime')
        
        draw.second()

    def second():
        ws = tk.Toplevel()
        ws.title("Path Use Quantity")
        canvas = tk.Canvas(ws, width=1290, height=857)
        canvas.pack()
        circle2 = lambda x, y, color: canvas.create_oval(20+x, 20+y, 30+x, 30+y, fill=color)
        bg2 = tk.PhotoImage(file = r"D:\Users\Dennis\Documents\Luc\python 3\Data-points-map\Layout FP plant (1).gif")
        canvas.create_image(0, 0,image=bg2, anchor=tk.NW)
        F2 = circle2(300, 450, "lime")
        B2 = circle2(430, 450, 'lime')
        J2 = circle2(350, 490, 'black')
        I2 = circle2(500, 480, 'black')
        H2 = circle2(540, 480, 'black')
        K2 = circle2(555, 425, 'blue')
        D2 = circle2(520, 430, 'lime')
        N2 = circle2(625, 420, 'blue')
        M2 = circle2(625, 280, 'blue')
        L2 = circle2(900, 270, 'blue')
        C2 = circle2(920, 150, 'lime')
        P2 = circle2(680, 480, 'blue')
        Q2 = circle2(760, 500, 'blue')
        E2 = circle2(630, 510, 'lime')
        A2 = circle2(680, 570, 'lime')
        G2 = circle2(760, 570, 'lime')
        
        draw.MainLoop()
        
class Product:
    def __init__(self, Datum, Locatie, Batch_code, Aantal) -> None:
        self.Datum = Datum
        self.Locatie = Locatie
        self.Batch_code = Batch_code
        self.Aantal = Aantal
    def getDatum(self):
        return self.Datum

path = r"D:\Users\Dennis\Documents\Luc\python 3\Data-points-map\data.xlsx"
wb_obj = exel.load_workbook(path)
sheet_obj = wb_obj.active
initialcode = sheet_obj.cell(row=2, column=3)
data = []
#TODO: aan menno vragen waar ik moet beginnen
for row in range(10, sheet_obj.max_row):
    rowdata = [sheet_obj.cell(row=row, column=i).value for i in range(1, sheet_obj.max_column)]
    data.append(rowdata)
datafiltered = []
for entry in data:
    datafiltered.append(entry[0])
    datafiltered.append(entry[1])
    datafiltered.append(entry[2])
    datafiltered.append(entry[4])

prev=None
for Product_ in datafiltered:
    current = None
    while current == prev and prev or current !=  None:
        print (2)

draw.main()

from collections import defaultdict

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


#this is copied

def BFS_SP(graph, start, goal):
    explored = []
     
    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]
     
    # If the desired node is
    # reached
    if start == goal:
        print("Same Node")
        return
     
    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]
         
        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]
             
            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                 
                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    print("Shortest path = ", *new_path)
                    return
            explored.append(node)
 
    # Condition when the nodes
    # are not connected
    print("So sorry, but a connecting"\
                "path doesn't exist :(")
    return
 
# Driver Code
if __name__ == "__main__":
     
    # Graph using dictionaries
    graph = {'A': ['B', 'E', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F', 'G'],
            'D': ['B', 'E'],
            'E': ['A', 'B', 'D'],
            'F': ['C'],
            'G': ['C']}
     
    # Function Call
    BFS_SP(graph, 'A', 'D')
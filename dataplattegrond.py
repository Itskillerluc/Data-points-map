
class path:
    paths = {}

    used = {
        'A':False,
        'B':False,
        'C':False,
        'D':False,
        'E':False,
        'F':False,
        'G':False,
        'H':False,
        'I':False,
        'J':False
    }

    plattegrond = {
        'A':['C'],
        'B':['C', 'F'],
        'C':['A', 'B', 'D'],
        'D':['C', 'E', 'G', 'I'],
        'E':['D'],
        'F':['B'],
        'G':['D', 'H', 'J'],
        'H':['G'],
        'I':['D', 'J'],
        'J':['G', 'I']
    }

    lengths = {
        'AC':1,
        'BC':1,
        'BF':3,
        'CD':2,
        'DE':3,
        'DI':2,
        'DG':2,
        'GH':3,
        'IJ':4,
        'JG':5,
        'CA':1,
        'CB':1,
        'FB':3,
        'DC':2,
        'ED':3,
        'ID':2,
        'GD':2,
        'HG':3,
        'JI':4,
        'GJ':5,
    }

    class PathToEnd:

        def __init__(self, path, lengths:list) -> None:
            self.path = path
            self.lengths = lengths

        def getPath(self):
            return self.path

        def getTotalLength(self):
            total = None
            for length in self.lengths:
                total =+ length
            return total

    def calclengths(self, path:list):
        path=[path[i//2] for i in range(len(path)*2)]
        sidesraw = ''.join(path)
        sidesraw = sidesraw[1:-1]
        sides = [sidesraw[i:i+2] for i in range(0, len(sidesraw), 2)]
        lengths = []
        for side in sides:
            lengths.append(self.lengths.get(side))
        return lengths

    def resetused(self):
        self.used = {
            'A':False,
            'B':False,
            'C':False,
            'D':False,
            'E':False,
            'F':False,
            'G':False,
            'H':False,
            'I':False,
            'J':False
        }


    def calcpath(self, Map, lengths, used,currentpath:list, end):
        temp_used = {
        'A':False,
        'B':False,
        'C':False,
        'D':False,
        'E':False,
        'F':False,
        'G':False,
        'H':False,
        'I':False,
        'J':False
    }

        currentnode = None if len(currentpath) == 0 else currentpath[len(currentpath)-1]
        
        for NODE in self.plattegrond:
            if temp_used[NODE]:
                adjacent = False
                for point in self.plattegrond[NODE]:
                    adjacent = point == currentnode
                if not adjacent:
                    temp_used.update({NODE:False})

        if currentpath[len(currentpath)-1] == end:
            temppath = self.PathToEnd(currentpath, self.calclengths(currentpath))
            self.paths.update(currentpath, temppath.getTotalLength)

        for node in self.plattegrond[currentnode]:
            if not used[node]:
                pass


    def calculate(self, Map, start, end):
        startpath = [start]
        self.calcpath(path, Map, self.lengths, self.used, startpath, end)
path.calculate(path,Map=path.plattegrond, start='A',end="B")
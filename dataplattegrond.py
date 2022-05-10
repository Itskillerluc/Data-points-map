
class path:
    paths = []

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
        return sides

    def calcpath(self, Map, lengths, used,currentpath:list, end):
        if currentpath.pop() == end:
            lines = self.calclines(currentpath)
            temppath = self.PathToEnd(currentpath, lin)
            self.paths.append(self.PathToEnd())


    def calculate(self, Map, start, end):
        startpath = [start]
        self.calcpath(Map, self.lengths, self.used, startpath, end)
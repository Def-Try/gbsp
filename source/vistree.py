from source.positioning import Vector

class Brush:
    def __init__(self, id, next, mins, maxs):
        self.id, self.next, self.mins, self.maxs = id, next, mins, maxs
        self.sides = []

class Portal:
    def __init__(self, id, plane, node):
        self.id, self.plane, self.node = id, plane, node
        self.nodes = []
        self.next = []
        self.sidefound = False
        self.size = None
        self.face = []

class VisNode:
    def __init__(self, parent, x1, y1, z1, x2, y2, z2):
        self.planenum = -1
        self.parent = parent
        self.mins, self.maxs = Vector(x1, y1, z2), Vector(x2, y2, z2)
        self.brushlist = None
        self.portals = None
        self.contents = 0

class VisTree:
    def __init__(self, mapx, mapy, mapz, mapw, maph, mapd):
        self.headnode = VisNode(self, mapx-1, mapy-1, mapz-1, mapx+mapw+1, mapy+maph+1, mapz+mapd+1)
        self.outside_node = VisNode(self, mapx-1, mapy-1, mapz-1, mapx+mapw+1, mapy+maph+1, mapz+mapd+1)
        self.mins = Vector(mapx, mapy, mapz)
        self.maxs = Vector(mapx+mapw, mapy+maph, mapz+mapd)
        self.leaked = False
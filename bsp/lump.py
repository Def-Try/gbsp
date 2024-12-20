from .globals import *

from .lumps.plane     import LUMP_Plane
from .lumps.verts     import LUMP_Vertex
from .lumps.edges     import LUMP_Edge
from .lumps.surfedges import LUMP_Surfedge
from .lumps.faces     import LUMP_Face

from enum import Enum

class LUMPTYPE:
    ENTITIES = 0
    PLANES = 1
    TEXDATA = 2
    VERTEXES = 3
    VISIBILITY = 4
    NODES = 5
    TEXINFO = 6
    FACES = 7

    EDGES = 12
    SURFEDGES = 13

LUMPS = {}

LUMPS[LUMPTYPE.PLANES]    = LUMP_Plane
LUMPS[LUMPTYPE.VERTEXES]  = LUMP_Vertex
LUMPS[LUMPTYPE.EDGES]     = LUMP_Edge
LUMPS[LUMPTYPE.SURFEDGES] = LUMP_Surfedge
LUMPS[LUMPTYPE.FACES]     = LUMP_Face

class Lump:
    def __init__(self, type, data):
        self.type = type
        self.data = data

    def __vbsp_write__(self) -> bytes:
        if not LUMPS.get(self.type):
            raise NotImplementedError(f"unknown lump type {self.type}")
        return LUMPS[self.type](self)

Lump.EMPTY = Lump(-1, None)

def __LUMP_Empty__(lump: Lump):
    return b''
LUMPS[-1] = __LUMP_Empty__

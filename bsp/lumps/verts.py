import struct

from source.positioning import Vector

from ..globals import *

def LUMP_Vertex(lump) -> bytes:
    body = b''
    if len(lump.data) > MAX_MAP_VERTS:
        raise OverflowError("too many vertices: {len(lump.data)} > {MAX_MAP_VERTS}")
    for vert in lump.data:
        body += struct.pack('fff', vert.x, vert.y, vert.z)
    return body

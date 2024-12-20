import struct

from source.positioning import Vector

from ..globals import *

def LUMP_Edge(lump) -> bytes:
    body = b''
    if len(lump.data) > MAX_MAP_EDGES:
        raise OverflowError("too many edges: {len(lump.data)} > {MAX_MAP_EDGES}")
    for edge in lump.data:
        body += struct.pack('S', edge[0])
        body += struct.pack('S', edge[1])
    return body

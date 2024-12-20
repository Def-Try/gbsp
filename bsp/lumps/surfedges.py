import struct

from source.positioning import Vector

from ..globals import *

def LUMP_Surfedge(lump) -> bytes:
    body = b''
    if len(lump.data) > MAX_MAP_SURFEDGES:
        raise OverflowError("too many surfedges: {len(lump.data)} > {MAX_MAP_SURFEDGES}")
    for edge in lump.data:
        body += struct.pack('i', edge[0])
        body += struct.pack('i', edge[1])
    return body

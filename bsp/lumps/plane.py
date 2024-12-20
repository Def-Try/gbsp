import struct

from source.positioning import Vector

from ..globals import *

def LUMP_Plane(lump) -> bytes:
    body = b''
    if len(lump.data) > MAX_MAP_PLANES:
        raise OverflowError("too many planes: {len(lump.data)} > {MAX_MAP_PLANES}")
    for plane in lump.data:
        body += struct.pack('fff', plane['normal'].x,
                                   plane['normal'].y,
                                   plane['normal'].z)
        body += struct.pack('f', plane['dist'])
        body += struct.pack('i', plane['type'])
    return body

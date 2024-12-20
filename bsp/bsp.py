import struct
import io

from .lump import Lump

class BSP:
    def __init__(self, version: int = 20):
        if version != 20:
            raise NotImplementedError(f"BSP version {version} not implemented")
        self.version = version
        self.lumps = {}
    def addLump(self, lump: Lump):
        self.lumps[lump.type] = lump
    def write(self, path):
        handle = open(path, 'wb')
        # header: VBSP
        handle.write(struct.pack("4c", b'V', b'B', b'S', b'P'))
        # version
        handle.write(struct.pack("i", self.version))
        body = b''
        # lump headers
        for i in range(64):  # HEADER_LUMPS=64
            lump = self.lumps.get(i, Lump.EMPTY)
            data = lump.__vbsp_write__()
            body = body + data
            handle.write(struct.pack("3i4c",
                             len(body)-len(data),
                             len(data), 0,
                             b'\0', b'\0', b'\0', b'\0'
                       ))
        # headers
        handle.write(body)

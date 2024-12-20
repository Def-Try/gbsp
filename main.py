import bsp
import vmf
from util.parse import parse_side
from util.flood import flood_entities
from util.portals import make_tree_portals
from source.vistree import VisTree, VisNode

src = "examples/box_with_entities.vmf" # single_multi-texture_brush.vmf
dst = "output/box_with_entities.bsp"

print(f"--- Prepare ---")

print(f"Loading VMF object from \"{src}\"...", end='', flush=True)
gvmf = vmf.VMF(src)
print(f"OK")
print(f"Creating BSP object...", end='', flush=True)
gbsp = bsp.BSP()
print(f"OK")

leaked = False

solids = gvmf.worlddata.get_all_for('solid')

print(f"--- ParseSolids ---")

vertices, planes = [], []
# [0] = texinfo [1] = texdata [2] = texdata [3] = textable
textures = [[], [], [], []]
for solid in solids:
    for side in solid.get_all_for('side'):
        parse_side(side, vertices, planes, textures)

print(f"{len(solids)} solids")
print(f"{len(vertices)} vertices")
print(f"{len(planes)} planes")
print(f"{len(textures[0])} texinfos")
print(f"{len(textures[1])} texdatas")
print(f"{len(textures[2])} textures")

vertices_lump = bsp.Lump(bsp.LUMPTYPE.VERTEXES, vertices)
planes_lump = bsp.Lump(bsp.LUMPTYPE.PLANES, planes)
gbsp.addLump(vertices_lump)
gbsp.addLump(planes_lump)

texinfo_lump = bsp.Lump(bsp.LUMPTYPE.TEXINFO, textures[0])
texdata_lump = bsp.Lump(bsp.LUMPTYPE.TEXDATA, textures[1])
# texdatastringtable_lump = bsp.Lump(bsp.LUMPTYPE.TEXDATASTRINGTABLE, textures[3])
# texdatastringdata_lump = bsp.Lump(bsp.LUMPTYPE.TEXDATASTRINGDATA, textures[2])

print(f"Creating VisTree object...", end='', flush=True)
vistree = VisTree(-1024*2, -1024*2, -1024*2, 2048*2, 2048*2, 2048*2)
print(f"OK")

portals = []

print(f"--- MakeTreePortals ---")
if not leaked and not make_tree_portals(gvmf, vistree, planes, portals):
    print("*** leaked! ***")
    leaked = True
elif leaked:
    print("skipped because leaked!")

print(f"--- FloodEntities ---")
if not leaked and not flood_entities(gvmf, vistree):
    print("*** leaked! ***")
    leaked = True
elif leaked:
    print("skipped because leaked!")

print(f"--- WriteBSP ---")
print(f"Writing BSP to \"{dst}\"...", end='', flush=True)
gbsp.write(dst)
print(f"OK")

print("GBSP done!")

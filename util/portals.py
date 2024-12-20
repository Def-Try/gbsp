from source.vistree import Portal

def make_headnode_portals(vmf, tree, planes, portals):
    node = tree.headnode

    tree.outside_node.planenum = -1
    tree.outside_node.brushlist = None
    tree.outside_node.portals = None
    tree.outside_node.contents = 0

    for i in range(0, 3, 1):
        for j in range(0, 2, 1):
            n = j*3+i
            portal = Portal(n, None, None)
            portals.append(portal)
            plane = planes[n]
            if i == 0: plane['normal'].x = 1 if j == 0 else -1
            if i == 1: plane['normal'].y = 1 if j == 0 else -1
            if i == 2: plane['normal'].z = 1 if j == 0 else -1

            if j > 0:
                plane['dist'] = -(tree.maxs.x if i == 0 else tree.maxs.y if i == 1 else tree.maxs.z)
            else:
                plane['dist'] =  (tree.mins.x if i == 0 else tree.mins.y if i == 1 else tree.mins.z)

def make_portals_r(vmf, node, planes, portals):
    print("implement volume check!!!")


def make_tree_portals(vmf, tree, planes, portals):
    print("Making Head node portals")
    make_headnode_portals(vmf, tree, planes, portals)
    print("Making recursive portals")
    make_portals_r(vmf, tree.headnode, planes, portals)
    return True
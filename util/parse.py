from source.positioning import Vector

def parse_side(side, vertices, planes, textures):
    for vertexes in side.get_all_for('vertices_plus'):
        for vertex_string in vertexes.get_all_for('v'):
            vertex = Vector(*map(float, vertex_string.split(" ")))
            if vertex in vertices: continue
            vertices.append(vertex)
    plane = side.get('plane')
    plane_vertices = [
        Vector(*map(float, vertex.split(" ")))
        for vertex in plane[1:-1].split(") (")
    ]
    plane_center = plane_vertices[0] + \
                   plane_vertices[1] + \
                   plane_vertices[2]
    planes.append({
        'normal': (plane_center/3).normal(),
        'dist': (plane_center/3).length(),
        'type': 4
    })

    texinfo, texdata, textable, texdata = textures[0], textures[1], textures[2], textures[3]
    
def ordenamientoTopologico(graph,source,path=[]):
    if source not in path:
        path.append(source)
        if source not in graph:
            return path
        for neighbour in graph[source]:
            path=ordenamientoTopologico(graph,neighbour,path)
    return path
graph = {"A":["B","C","D"], "B":["E"],"C":["F","G"],"D":["H"],"E":["I"],"F":["J"]}
path=ordenamientoTopologico(graph,"A")
print("".join(path))
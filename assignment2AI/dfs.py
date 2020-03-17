def add_vertex(vertex, h):
    global graph
    global heuristics
    heuristics.append(h)
    if vertex in graph:
        print(vertex, "already in graph")
    else:
        graph[vertex] = []


def add_edge(vertex1, vertex2, edge):
    global graph
    if vertex1 not in graph:
        print(vertex1, "not in graph")
    elif vertex2 not in graph:
        print(vertex2, "not in graph")
    else:
        graph[vertex1].append([vertex2, edge])
        graph[vertex2].append([vertex1, edge])


def depth_first_search(start_vertex, end_vertex):
    global visited
    if start_vertex == end_vertex:
        
        return [start_vertex]

    for v in graph[start_vertex]:
        if v[0] not in visited:
            visited.append(v[0])
            cost = cost + v[1]
            path = depth_first_search(v, end_vertex, cost)

            if path is not None:
                path.insert(0, start_vertex)
                return path


def print_result(start, end):
    print("Start vertex: ", start)
    print("End vertex: ", end)
    print("Results")
    depth_first_search(start, end)
    bfs(start, end)
    ucs()
    bestfirst()
    astar()
    print()


def add_vertex2(v, h):
    global graph
    global vertices
    global vcount
    global heuristics
    vcount += 1
    vertices.append(v)
    heuristics.append(h)
    if vcount > 1:
        for vertex in graph:
             vertex.append(0)
    temp = []
    for i in range(vcount):
        temp.append(0)
    graph.append(temp)


def add_edge2(v1, v2, edge):
    global graph
    global vertices
    if v1 not in vertices:
        print("error")
    elif v2 not in vertices:
        print("error")
    else:
        v1index = vertices.index(v1)
        v2index = vertices.index(v2)
        graph[v1index][v2index] = edge
        graph[v2index][v1index] = edge


def print_graph():
    print("Adjacency Matrix")
    global graph
    global vcount
    temp = "  "
    for i in range(vcount):
        t = i + 65
        temp = temp + chr(t) + " "
    print(temp)
    for i in range(vcount):
        temp = ""
        temp = temp + chr(i+65) + " "
        for j in range(vcount):
            if graph[i][j] != 0:
                temp += "1 "
            else:
                temp += "0 "
        print(temp)
    print()


def print_costs():
    print("Costs")
    global graph
    global vcount
    temp = "  "
    for i in range(vcount):
        t = i + 65
        temp = temp + chr(t) + " "
    print(temp)
    for i in range(vcount):
        temp = ""
        temp = temp + chr(i + 65) + " "
        for j in range(vcount):
            temp = temp + str(graph[i][j]) + " "
        print(temp)
    print()


def print_heuristics():
    print("Heuristic values")
    global heuristics
    global vcount
    temp = ""
    for i in range(vcount):
        t = i + 65
        temp = temp + chr(t) + ":(" + str(heuristics[i]) + ") "
    print(temp)
    print()


def dfs(start, end):

    print("DFS:")
#   visited = []
#    global vcount
#    global graph
#    for v in range(vcount):
#        visited.append(0)
#    cost = 0
#   temp = start + ": " + str(cost) + " "
#    for i in range(vcount):
#        for j in range(vcount):
#            if graph[i][j] != 0 & visited[j] == 0:
#                dfs2(chr(j+65), visited, cost + graph[i][j], temp, end)

    # global visited
    # if start == end:
    #    return [start]
    # vindex = vertices.index(start)
    # for v in graph[vindex]:
    #    if v != 0:


def dfs2(start, visited, cost, temp, end):
    temp = temp + str(start) + ": " + str(cost) + " "
    if start == end:
        return temp
    stindex = vertices.index(start)
    visited[stindex] = 1
    global vcount
    for i in range(vcount):
        for j in range(vcount):
            #if ord(j+65) == end:

            if graph[i][j] != 0 & visited[j] == 0:
                dfs2(j, visited, cost + graph[i][j], temp, end)


def bfs(start, end):
    print("BFS:")
    visited = []
    start_index = vertices.index(start)
    global graph
    global vcount
    for v in range(vcount):
        visited.append(0)

    visited[start_index] = 1
    queue = [start_index]
    while queue:
        temp = queue[0]
        queue.pop(0)
        print(temp)
        for i in range(vcount):
            if i != temp:
                if visited[i] == 0 & graph[temp][i] != 0:
                    visited[i] = 1
                    queue.append(i)



def ucs():
    print("Uniform cost search:")


def bestfirst():
    print("best first search:")


def astar():
    print("A*:")


# driver
vertices = []
vcount = 0
graph = {}
heuristics = []
visited = []

# graph1
add_vertex('A', 15)
add_vertex('B', 14)
add_vertex('C', 10)
add_vertex("D", 2)
add_vertex("E", 0)
add_vertex("F", 5)
add_vertex("G", 9)
add_vertex("H", 11)
add_edge("A", "B", 3)
add_edge("A", "H", 4)
add_edge("B", "C", 4)
add_edge("B", "H", 5)
add_edge("C", "D", 8)
add_edge("C", "G", 3)
add_edge("D", "E", 2)
add_edge("D", "F", 3)
add_edge("D", "G", 8)
add_edge("G", "F", 4)
add_edge("G", "H", 2)

# print_graph()
# print_costs()
# print_heuristics()
print_result("A", "E")

print("------------------------")









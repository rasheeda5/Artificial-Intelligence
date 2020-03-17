def add_vertex(vertex):
    global graph
    if vertex in graph:
        print(vertex, "already in graph")
    else:
        graph[vertex] = []


def add_edge(vertex1, vertex2):
    global graph
    if vertex1 not in graph:
        print(vertex1, "not in graph")
    elif vertex2 not in graph:
        print(vertex2, "not in graph")
    else:
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)


def depth_first_search(start_vertex, end_vertex):
    global visited
    if start_vertex == end_vertex:
        return [start_vertex]

    for v in graph[start_vertex]:
        if v not in visited:
            visited.append(v)
            path = depth_first_search(v, end_vertex)

            if path is not None:
                path.insert(0, start_vertex)
                return path


def breadth_first_search(start_vertex, end_vertex):
    global queue
    global visited
    queue.append(start_vertex)
    visited.append(start_vertex)
    while queue:
        temp = queue[0]
        print(temp)
        if temp == end_vertex:
            break
        queue.remove(temp)
        for v in graph[temp]:
            if v not in visited:
                queue.append(v)
                visited.append(v)


def iterative_deepening_search(start_vertex, end_vertex, max):
    global graph
    global visited
    for depth in range(0, max):
        ans = ids([start_vertex], end_vertex, max)
        if ans is None:
            continue
        return ans


def ids(path, end_vertex, max):
    current = path[-1]
    if current == end_vertex:
        return path
    if max <= 0:
        return None
    for i in graph[current]:
        new_path = list(path)
        new_path.append(i)
        ans = ids(new_path, end_vertex, max-1)
        if ans is not None:
            return result


# driver
graph = {}

add_vertex("Arad")
add_vertex("Zerind")
add_vertex("Odarea")
add_vertex("Timisoara")
add_vertex("Sibiu")
add_vertex("Farara")
add_vertex("Lugoj")
add_vertex("Mehadia")
add_vertex("Dobreta")
add_vertex("Rimnicu Vilcea")
add_vertex("Craiova")
add_vertex("Pitesti")
add_vertex("Bucharest")
add_vertex("Urziceni")
add_vertex("Giurgui")
add_vertex("Neamt")
add_vertex("Iasi")
add_vertex("Vaslui")
add_vertex("Hirsova")
add_vertex("Eforie")

add_edge("Arad", "Zerind")
add_edge("Arad", "Sibiu")
add_edge("Arad", "Timisoara")
add_edge("Odarea", "Zerind")
add_edge("Odarea", "Sibiu")
add_edge("Farara", "Sibiu")
add_edge("Sibiu", "Rimnicu Vilcea")
add_edge("Timisoara", "Lugoj")
add_edge("Lugoj", "Mehadia")
add_edge("Mehadia", "Dobreta")
add_edge("Dobreta", "Craiova")
add_edge("Craiova", "Rimnicu Vilcea")
add_edge("Rimnicu Vilcea", "Pitesti")
add_edge("Craiova", "Pitesti")
add_edge("Bucharest", "Pitesti")
add_edge("Bucharest", "Farara")
add_edge("Bucharest", "Giurgui")
add_edge("Bucharest", "Urziceni")
add_edge("Hirsova", "Urziceni")
add_edge("Hirsova", "Eforie")
add_edge("Hirsova", "Vaslui")
add_edge("Iasi", "Vaslui")
add_edge("Iasi", "Neamt")

print("Graph")
print(graph)
print()
print("Depth First Search")
visited = ["Arad"]
result = depth_first_search("Arad", "Bucharest")
for i in result:
    print(i)
visited.clear()
print()
queue = []
print("Breadth First Search")
print(breadth_first_search("Arad", "Bucharest"))
visited.clear()
print()
print("Iterative Deepening Search")
result = iterative_deepening_search("Arad", "Bucharest", 3)
for i in result:
    print(i)
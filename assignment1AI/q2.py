def solution_space(start_state, goal_state):
    global queue
    global choices
    queue.append(start_state)
    choices.append(start_state)
    while queue:
        temp = queue[0][:]
        print(temp)
        if temp == goal_state:
            break
        opt1 = swap(temp, 'a', '_')
        temp = queue[0][:]
        opt2 = swap(temp, 'b', '_')
        temp = queue[0][:]
        opt3 = swap(temp, 'y', '_')
        temp = queue[0][:]
        opt4 = swap(temp, 'z', '_')
        temp = queue[0][:]
        queue.remove(temp)
        if opt1 not in choices:
            queue.append(opt1)
            choices.append(opt1)
        if opt2 not in choices:
            queue.append(opt2)
            choices.append(opt2)
        if opt3 not in choices:
            queue.append(opt3)
            choices.append(opt3)
        if opt4 not in choices:
            queue.append(opt4)
            choices.append(opt4)


def swap(current, char1, char2):
    index_char1 = current.index(char1)
    index_char2 = current.index(char2)
    if char1 == 'a':
        if index_char2 == (index_char1 + 1) or index_char2 == (index_char1 + 2):
            current[index_char1], current[index_char2] = current[index_char2], current[index_char1]
    elif char1 == 'b':
        if index_char2 == (index_char1 + 1) or index_char2 == (index_char1 + 2):
            current[index_char1], current[index_char2] = current[index_char2], current[index_char1]
    elif char1 == 'y':
        if index_char2 == (index_char1 - 1) or index_char2 == (index_char1 - 2):
            current[index_char1], current[index_char2] = current[index_char2], current[index_char1]
    else:
        if index_char2 == (index_char1 - 1) or index_char2 == (index_char1 - 2):
            current[index_char1], current[index_char2] = current[index_char2], current[index_char1]

    return current


def depth_first_search(start_state, goal_state):
    global choices
    if start_state == goal_state:
        return [start_state]
    for v in graph[start_state]:
        if v not in choices:
            choices.append(v)
            path = depth_first_search(v, goal_state)
            if path is not None:
                path.insert(0, start_state)
                return path


def generate_graph(start_state):
    global graph
    graph[start_state] = []
    temp = start_state[:]
    opt1 = swap(temp, 'a', '_')
    if not opt1 == start_state[:]:
        graph[start_state].append(opt1)
    if opt1 not in graph:
        generate_graph(opt1)
    temp = start_state[:]
    opt2 = swap(temp, 'b', '_')
    if not opt2 == start_state[:]:
        graph[start_state].append(opt2)
    if opt2 not in graph:
        generate_graph(opt2)
    temp = start_state[:]
    opt3 = swap(temp, 'y', '_')
    if not opt3 == start_state[:]:
        graph[start_state].append(opt3)
    if opt3 not in graph:
        generate_graph(opt3)
    temp = start_state[:]
    opt4 = swap(temp, 'z', '_')
    if not opt4 == start_state[:]:
        graph[start_state].append(opt4)
    if opt4 not in graph:
        generate_graph(opt4)


# driver
start = ['a', 'b', '_', 'y', 'z']
goal = ['y', 'z', '_', 'a', 'b']
choices = []
queue = []
print("Solution Space Using Breadth First Search")
print(solution_space(start, goal))
print()
choices.clear()
choices = ['a', 'b', '_', 'y', 'z']
graph = {}
print("Solution Space Using Depth First Search")
generate_graph(start)
result = depth_first_search(start, goal)
for i in result:
    print(i)





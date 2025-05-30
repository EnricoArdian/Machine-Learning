graph = {
    '1' : ['2', '3'],
    '2' : ['5', '7'],
    '3' : ['4', '6'],
    '5' : ['8'],
    '7' : ['10'],
    '4' : ['7', '9'],
    '6' : ['9'],
    '8' : ['10'],
    '10' : [],
    '9' : ['10'],
}

visited = []
queue = []

def bfs(visited, graph, start_node, end_node):
    visited.append(start_node)
    queue.append(start_node)

    while queue:
        m = queue.pop(0)
        print(f"|{m}|", end=" ")

        if m == end_node:
            break

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

start_node = input("masukkan angka awal : ")
end_node = input("masukkan angka akhir : ")

try:
    start_node = str(int(start_node))
    end_node = str(int(end_node))
except ValueError:
    print("Node harus berupa angka.")
    exit()

# Menangani kasus di mana node tidak ada dalam graf
if start_node not in graph or end_node not in graph:
    print("Node tidak ada dalam graf.")
else:
    print("following is the breadth-first search")
    bfs(visited, graph, start_node, end_node)

import heapq  # Importamos la librería heapq para manejar la cola de prioridad

# Función que implementa el algoritmo de Prim
def prim(graph, start):
    mst = []  # Lista para almacenar las aristas del árbol de expansión mínima
    visited = set()  # Conjunto para almacenar los nodos visitados
    edges = [(0, start, start)]  # Cola de prioridad de aristas, inicializada con el nodo de inicio

    while edges:  # Mientras haya aristas en la cola de prioridad
        weight, current_node, next_node = heapq.heappop(edges)  # Obtenemos la arista con menor peso
        if next_node not in visited:  # Si el nodo destino no ha sido visitado
            visited.add(next_node)  # Marcamos el nodo destino como visitado
            mst.append((current_node, next_node, weight))  # Añadimos la arista al árbol de expansión mínima

            # Añadimos las aristas adyacentes al nodo destino a la cola de prioridad
            for neighbor, edge_weight in graph[next_node].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (edge_weight, next_node, neighbor))

    return mst[1:]  # Retornamos el árbol de expansión mínima sin la arista inicial (start, start)

# Función para crear el grafo de ejemplo
def create_graph():
    graph = {
        "Ana": {"Fabian": 5, "Carol": 1, "David": 6, "Laura":4},
        "Fabian": {"Ana": 5, "Carol": 3, "David": 2},
        "Carol": {"David": 4, "Fabian": 3, "Ana": 4, "Alejo": 3},
        "David": {"Alejo": 8, "Fabian": 9, "Carol": 7},
        "Alejo": {"Ana": 2, "Carol": 1, "David": 3, "Alejo": 9},
        "Juan": {"Ana": 5, "Fabian": 3, "Carol": 4, "David": 5, "Alejo": 7},
        "Laura": {"Fabian": 6, "Carol": 2, "David": 4},
        "Saul": {"Juan": 7, "Laura": 3}
        
    }
    return graph

# Función para mostrar las recomendaciones de amistad basadas en el árbol de expansión mínima
def show_friend_recommendations(mst, person):
    recommendations = []  # Lista para almacenar las recomendaciones
    for edge in mst:  # Recorremos las aristas del árbol de expansión mínima
        if edge[0] == person:  # Si la persona está en el nodo origen
            recommendations.append((edge[1], edge[2]))  # Añadimos el nodo destino y el peso
        elif edge[1] == person:  # Si la persona está en el nodo destino
            recommendations.append((edge[0], edge[2]))  # Añadimos el nodo origen y el peso

    recommendations.sort(key=lambda x: x[1])  # Ordenamos las recomendaciones por peso
    return recommendations

if __name__ == "__main__":
    graph = create_graph()  # Creamos el grafo de ejemplo
    start_node = input("Ingrese el nombre de la persona: ")  # Solicitamos el nombre de la persona al usuario
    if start_node in graph:  # Si la persona está en el grafo
        mst = prim(graph, start_node)  # Calculamos el árbol de expansión mínima
        print("Red de conexiones mínima:", mst)  # Mostramos el árbol de expansión mínima
        recommendations = show_friend_recommendations(mst, start_node)  # Obtenemos las recomendaciones de amistad
        print("Recomendaciones de amistad para {}:".format(start_node))  # Mostramos las recomendaciones
        for friend, weight in recommendations:
            print("  - {}: {}".format(friend, weight))
    else:
        print("La persona ingresada no se encuentra en la red social.")  # Informamos si la persona no está en el grafo
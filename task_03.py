import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = [[] for _ in range(num_vertices)]

    def add_edge(self, source, destination, weight):
        self.adjacency_list[source].append((destination, weight))

    def visualize_graph(self):
        G = nx.Graph()
        for source in range(self.num_vertices):
            for destination, weight in self.adjacency_list[source]:
                G.add_edge(source, destination, weight=weight)

        pos = nx.spring_layout(G)  # Позиціонуємо вершини графа
        nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=12, font_weight="bold")
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.title("Візуалізація графа")
        plt.show()

    def dijkstra(self, source):
        # Ініціалізуємо масив для збереження найкоротших відстаней
        distances = [float('inf')] * self.num_vertices
        distances[source] = 0

        # Ініціалізуємо бінарну купу для використання її як пріоритетна черга
        priority_queue = [(0, source)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Якщо поточна відстань до поточної вершини вже більша, ніж відома найкоротша відстань,
            # пропускаємо цю вершину
            if current_distance > distances[current_vertex]:
                continue

            # Оновлюємо відстані до всіх сусідніх вершин
            for neighbor, weight in self.adjacency_list[current_vertex]:
                distance = current_distance + weight
                # Якщо ми знайшли шлях, який коротший за відомий раніше, оновлюємо відстань
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    # Додаємо сусідню вершину в чергу для подальшого розгляду
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

def main():
    num_vertices = 6
    graph = Graph(num_vertices)
    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 3, 6)
    graph.add_edge(1, 2, 2)
    graph.add_edge(2, 4, 4)
    graph.add_edge(2, 5, 2)
    graph.add_edge(2, 3, 7)
    graph.add_edge(3, 4, 1)
    graph.add_edge(4, 5, 2)

    source_vertex = 0
    shortest_distances = graph.dijkstra(source_vertex)

    for vertex in range(num_vertices):
        print(f"Найкоротший шлях від вершини {source_vertex} до вершини {vertex} = {shortest_distances[vertex]}")

    graph.visualize_graph()
    
if __name__ == "__main__":
    main()

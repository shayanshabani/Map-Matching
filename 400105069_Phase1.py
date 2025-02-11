# TODO: You should implement this from scratch and you cannot use any library (such as networkx) for finding the shortest path.
from math import radians, sin, cos, sqrt, atan2
import pandas as pd

def find_shotest_path(start_node, end_node, graph):
    """
    Find the shortest path between two nodes in a graph.
    :param start_node: The start node
    :param end_node: The end node
    :param graph: The graph
    :return: The shortest path. It is a list of node_ids from start_node to end_node.
    Note that you use all of the data in "pasdaran_streets" dataset appropriately such as "street_length" and "one_way".
    """
    # TODO
    df = pd.DataFrame(graph)
    another_graph = {}
    for index, row in df.iterrows():
        if row['u'] not in another_graph:
            another_graph[row['u']] = {}
        if row['v'] not in another_graph:
            another_graph[row['v']] = {}
        another_graph[row['u']][row['v']] = row['length']
        another_graph[row['v']][row['u']] = row['length']
    another_start_node, _ = find_closest_node(start_node[0], start_node[1], df)
    another_end_node, _ = find_closest_node(end_node[0], end_node[1], df)
    shortest_path = dijkstra(another_graph, another_start_node, another_end_node)
    
    return shortest_path


def dijkstra(graph, start, end):
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0
    visited = set()
    previous_nodes = {}
    while visited != set(shortest_distances):
        current_node = min (
            {node: shortest_distances[node] for node in shortest_distances if node not in visited},
            key=shortest_distances.get
        )
        visited.add(current_node)
        for neighbor, weight in graph[current_node].items():
            if weight + shortest_distances[current_node] < shortest_distances[neighbor]:
                shortest_distances[neighbor] = weight + shortest_distances[current_node]
                previous_nodes[neighbor] = current_node
    path = []
    each_distance = []
    while end is not None:
        path.append(end)
        each_distance.append(shortest_distances[end])
        end = previous_nodes.get(end)
        
    if shortest_distances[path[-1]] != float('inf'):
        return path[::-1], each_distance[::-1]
    return None, None


def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371.0
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    
    return distance


def find_closest_node(lat, lon, df):
    closest_node = None
    closest_distance = float('inf')
    for index, row in df.iterrows():
        distance = calculate_distance(lat, lon, row['u_lat'], row['u_lon'])
        if distance < closest_distance:
            closest_distance = distance
            closest_node = row['u']
            
    return closest_node, closest_distance
import heapq
import numpy as np

class PriorityQueue:
    def __init__(self):
        self.elements = []
    def empty(self):
        return len(self.elements) == 0
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    def get(self):
        return heapq.heappop(self.elements)[1]


class DirectedGraph(object):
  def __init__(self, index_set, edge_set):
    # The index set of the graph
    self.index_set = index_set
    # This is a set of triples: (start, end, weight)
    self.edge_set = edge_set

  def neighbors(self, node):
    return [e[1] for e in self.edge_set if e[0] == node]

  def cost(self, start, end):
    for edge in self.edge_set:
      if edge[0] == start and edge[1] == end:
        return edge[2]
    return None
  
  def astar(self, start_node, end_node, heuristic):
    # The open set is the set of nodes we have discovered but not yet
    # visited.  It is a priority queue, with the lowest cost node at the
    # top.
    open_set = PriorityQueue()
    open_set.put(start_node, 0)

    # The closed set is the set of nodes we have visited.
    closed_set = set()

    # The came_from dictionary is used to reconstruct the path at the end.
    came_from = {}

    # The g_score dictionary stores the cost of the cheapest path from
    # the start node to a given node.
    g_score = {node : np.inf for node in self.index_set}
    g_score[start_node] = 0

    # The f_score dictionary stores the cost of the cheapest path from
    # the start node to the goal by passing by a given node.
    f_score = {}
    f_score[start_node] = heuristic[start_node]

    print("Start heap: ", open_set.elements)

    while not open_set.empty():
      current = open_set.get()

      if current == end_node:
        print("Found path with cost", g_score[current])
        print("Final f_score dictionary", f_score)
        return True

      # closed_set.add(current)

      for neighbor in self.neighbors(current):
        # if neighbor in closed_set:
        #   continue

        tentative_g_score = g_score[current] + self.cost(current, neighbor)

        if tentative_g_score < g_score[neighbor]:
          came_from[neighbor] = current
          print("coming from", current, "to", neighbor)
          g_score[neighbor] = tentative_g_score
          f_score[neighbor] = tentative_g_score + heuristic[neighbor]
          open_set.put(neighbor, f_score[neighbor])
          print("the heap is now: ", open_set.elements)
    return None
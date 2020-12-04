class Graph():
  class Node():
    def __init__(self, data, *args):
      self.data = data
      self.edges = []
      
      for item in args:
        self.edges.append(item)

  def __init__(self, json):
    self._nodes = {}
    self._jsonToGraph(json)

  def _jsonToGraph(self, json):
    for node in json:
      data = node['name']
      new_node = self.Node(data, *node['prerequisites'])
      self._nodes[data] = new_node
    
  def number_edges(self, data):
    return len(self._nodes[data].edges)
  
  def traversal_order(self):
    visited = {}
    components = {}
    index = 0

    def dfs(node):
      visited[node.data] = index 
      for edge in node.edges:
        if visited.get(edge) is not None and visited[edge] != index:
          components.pop(visited[edge], None)
        
        dfs(self._nodes[edge])
      
      components[index].append(node.data)
    
    
    for node in self._nodes:
      components[index] = []
      dfs(self._nodes[node])
      index += 1
    
    print(components)

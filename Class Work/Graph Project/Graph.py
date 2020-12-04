class Graph():
  class Node():
    def __init__(self, data, *args):
      self.data = data
      self.edges = []
      
      for item in args:
        self.edges.append(item)

  def __init__(self, json):
    self._nodes = []
    self._jsonToGraph(json)

  def _jsonToGraph(self, json):
    for node in json:
      new_node = self.Node(node['name'], *node['prerequisites'])
      self._nodes.append(new_node)

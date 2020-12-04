import json
from Graph import Graph

with open("test.json") as test:
  data = json.load(test)


graph = Graph(data)
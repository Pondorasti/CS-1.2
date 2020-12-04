import json
from Graph import Graph

def numPrereqs(graph, course):
  return f"Course {course} has {graph.number_edges(course)} prerequisites."

with open("test.json") as test:
  data = json.load(test)

courses_graph = Graph(data)

print(numPrereqs(courses_graph, "FEW 2.3"))
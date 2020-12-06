import json
from Graph import Graph

def numPrereqs(graph, course):
  return f"Course {course} has {graph.number_edges(course)} prerequisites."

def scheduler(coursesJson):
  courses_graph = Graph(coursesJson)
  components = courses_graph.connected_components()
  for courses in components.values():
    for course in courses:
      print(course)


with open("test.json") as test:
  coursesJson = json.load(test)

courses_graph = Graph(coursesJson)
print(numPrereqs(courses_graph, "FEW 2.3"))

scheduler(coursesJson)
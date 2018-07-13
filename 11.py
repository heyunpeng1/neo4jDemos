#run cql语句
from py2neo import Graph

graph = Graph(password='asdfasdfa')
data = graph.run('MATCH (p:Person) RETURN p LIMIT 5')
print(list(data))
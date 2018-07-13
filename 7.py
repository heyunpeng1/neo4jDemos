#neo4j 查询
from py2neo import Node, Relationship, Graph

from py2neo import Graph
graph = Graph(password='asdfasdfa')
print(graph.run("MATCH (a:Person) RETURN a.name LIMIT 3").to_table())
print(graph.evaluate("MATCH (a:Person) RETURN count(a)"))

print(graph.run('MATCH (p:Person) return p')) #返回的是py2neo.database.Cursor
data = graph.run('MATCH (p:Person) return p').to_table()
print(data)


nodeMatch = graph.nodes.match("Person", age='33')
print(len(nodeMatch))
print(nodeMatch.first()['name'])
for node in nodeMatch:
    print(node['name'])




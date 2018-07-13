#删除节点
from py2neo import Graph

# graph = Graph(password='asdfasdfa')
# node = graph.nodes.match("Person", name='Jack', age=44).first()
# # relationship = graph.match_one(rel_type='KNOWS')
# # graph.delete(relationship)
# graph.delete(node)

#删除全部
graph = Graph(password='asdfasdfa')
nodes = graph.nodes.match("老师")
for node in nodes:
    graph.delete(node)
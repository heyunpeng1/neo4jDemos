#更新数据库某一个节点的值
from py2neo import Graph, Node

graph = Graph(password='asdfasdfa')
node = graph.nodes.match("Person", name='Jack').first()
node['age'] = 88
graph.push(node)


node = graph.nodes.match("Person", name='Jack', age=88).first()
node['age'] = 44
graph.push(node)
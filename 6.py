#Graph新增数据，入库
#如何安装neo4j https://neo4j.com/download-thanks-beta/?edition=enterprise&release=3.5.0-alpha04&flavour=unix&_ga=2.217740886.1555121913.1531290048-1608792872.1531290048
#运行这段代码需要先安装neo4j数据库
from py2neo import Graph
from py2neo import Node, Relationship, Graph
# graph_1 = Graph()
# graph_2 = Graph(host="localhost")
# graph_3 = Graph("http://localhost:7474/db/data/")

# a = Node('Person', name='Alice')
# b = Node('Person', name='Bob')
# r = Relationship(a, 'KNOWS', b)
# s = a | b | r
# graph = Graph(password='asdfasdfa')
# graph.create(s)

#单独添加单个 Node 或 Relationship
graph = Graph(password='asdfasdfa')
a = Node('Person', name='小江')
graph.create(a)
b = Node('Person', name='许慧')
ab = Relationship(a, 'KNOWS', b)
graph.create(ab)

# graph = Graph(password='asdfasdfa')
a = Node('Person', name='hh', age='33')
graph.create(a)
b = Node('Person', name='yy', age='30')
ab = Relationship(a, 'KNOWS', b)
graph.create(ab)



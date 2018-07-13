#Graph新增数据，入库
#如何安装参考官网https://neo4j.com/
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



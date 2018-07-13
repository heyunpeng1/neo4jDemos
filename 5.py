#Walkable 是增加了遍历信息的 Subgraph，我们通过 + 号便可以构建一个 Walkable 对象
from py2neo import Node, Relationship
from py2neo import walk
a = Node('Person', name='Alice')
b = Node('Person', name='Bob')
c = Node('Person', name='Mike')
ab = Relationship(a, "KNOWS", b)
ac = Relationship(a, "KNOWS", c)
w = ab + Relationship(b, "LIKES", c) + ac
for item in walk(w):
    print(item)

print(w.start_node)
print(w.end_node)
print(w.nodes)
print(w.relationships)
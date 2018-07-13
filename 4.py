#子图
from py2neo import Node, Relationship

a = Node('Person', name='Alice')
b = Node('Person', name='Bob')
r = Relationship(a, 'KNOWS', b)
s = a | b | r

ns = s.nodes
rs = s.relationships
for node in ns:
    print(node)
for r in rs:
    print(r)

s1 = a | b | r
s2 = a | b
s = s1 & s2
print(s)

keys = s.keys
nodes = s.nodes
for node in nodes:
    print(node)
print(s.labels)

print(s.relationships)
print(s.types)

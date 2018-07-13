#简单的创建两个对象，并建立关系
from py2neo import Node, Relationship

a = Node('Person', name='Alice')
b = Node('Person', name='Bob')
r = Relationship(a, 'KNOWS', b)
print(a, b, r)
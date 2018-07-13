#transaction about commit
from py2neo import Graph, Node, Relationship
graph = Graph(password='asdfasdfa')
# tx = graph.begin()
# # a = Node("Person", name="Lilei")
# # tx.create(a)
# # b = Node("Person", name="Hanmeimei")
# # ab = Relationship(a, "KNOWS", b)
# # tx.create(ab)
# # tx.commit()
# # graph.exists(ab)

tx = graph.begin()
a = Node("Person", name="Jack")
tx.create(a)
# b = Node("Person", name="Hanmeimei")
b = graph.nodes[25]
ab = Relationship(a, "KNOWS", b)
tx.create(ab)
tx.commit()
print(graph.exists(ab))
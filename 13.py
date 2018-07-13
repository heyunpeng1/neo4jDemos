from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo
from py2neo import Graph

class Movie(GraphObject):
    __primarykey__ = "title"

    title = Property()
    tag_line = Property("tagline")
    released = Property()

    actors = RelatedFrom("Person", "ACTED_IN")
    directors = RelatedFrom("Person", "DIRECTED")
    producers = RelatedFrom("Person", "PRODUCED")


class Person(GraphObject):
    __primarykey__ = "name"

    name = Property()
    born = Property()

    acted_in = RelatedTo(Movie)
    directed = RelatedTo(Movie)
    produced = RelatedTo(Movie)

graph = Graph(password='asdfasdfa')
# keanu=Person()
# keanu.name='keanu'
# keanu.born = 1956
# bill_and_ted = Movie()
# bill_and_ted.title = "Bill & Ted's Excellent Adventure"
# bill_and_ted.released = '哥伦比亚电影公司'
# keanu.acted_in.add(bill_and_ted)
# graph.push(keanu)


keanu = Person.match(graph, "keanu").first()
keanu.born = 1957 #更新
bill_and_ted = Movie.match(graph, "Bill & Ted's Excellent Adventure").first()
bill_and_ted.released = '中国电影公司'
bill_and_ted.tag_line = 'yyy'
keanu.acted_in.add(bill_and_ted)
graph.push(bill_and_ted)
graph.push(keanu)
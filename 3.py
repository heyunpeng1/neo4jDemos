#更新实体属性
from py2neo import Node, Relationship

a = Node('Person', name='Alice')
b = Node('Person', name='Bob')
r = Relationship(a, 'KNOWS', b)
a['age'] = 20
a.setdefault('location', '北京')

data = {
    'name': 'Amy',
    'age': 21
}
a.update(data)
b['age'] = 21
r['time'] = '2017/08/31'
print(a, b, r)
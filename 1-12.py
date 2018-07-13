#这里我通过前面的小例子实践一个班级关系维护录
#学生，老师是实体，关系包括 同学，师生，铁哥们，闺蜜，情侣
from py2neo import Graph, Node, Relationship
#10个学生
a1 = Node('学生', name='二狗', age=21, sex='男', gradClass='2年3班')
a2 = Node('学生', name='铁柱', age=22, sex='男', gradClass='2年3班')
a3 = Node('学生', name='二蛋', age=21, sex='男', gradClass='2年3班')
a4 = Node('学生', name='小新', age=21, sex='男', gradClass='2年3班')
a5 = Node('学生', name='阿呆', age=21, sex='男', gradClass='2年3班')
a6 = Node('学生', name='正男', age=20, sex='男', gradClass='2年3班')

b1 = Node('学生', name='范冰冰', age=20, sex='女', gradClass='2年3班')
b2 = Node('学生', name='凤姐', age=20, sex='女', gradClass='2年3班')

allStuNodes = [a1,a2,a3,a4,a5,a6,b1,b2]
boyStuNodes = [a1,a2,a3,a4,a5,a6]
girlStuNodes = [b1,b2]
c1 = Node('老师', name='冯小刚', age=50, sex='男', gradClass='2年3班')

graph = Graph(password='asdfasdfa')
#所有学生建立同学关系网
# for stu in allStuNodes:
#     for stu_ in allStuNodes:
#         if stu != stu_:
#             r = Relationship(stu, '同学', stu_)
#             graph.create(r)

#所有学生与老师建立师生关系
for stu in allStuNodes:
    r = Relationship(stu, '师生', c1)
    graph.create(r)

#建立情侣关系
for stu in boyStuNodes:
    r = Relationship(stu, '炮友', b1)
    graph.create(r)

#师生情
for stu in girlStuNodes:
    r = Relationship(stu, '师生乱情', c1)
    graph.create(r)
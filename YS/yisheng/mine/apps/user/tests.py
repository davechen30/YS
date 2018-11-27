#! / usr / bin / python
# coding:utf8
#
# from types import MethodType
# class Student(object):
#     # __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
#     pass
#
# s1 = Student()
# s2 = Student()
# s1.name = 'hi'
# s2.name = 'haas'
# # s.__slots__ = ('name', 'age','jj')
# # print(s.__slots__)
# def getName(self):
#     return self.name
#
# s1.getName = MethodType(getName,s1)
# s2.getName = MethodType(getName,s2)
# print(s1.getName())
# print(s2.getName())
#
# dic = {'name':'dave','age':23}
# dic_item = [('name', 'dave'), ('age', 23)]
# print(list(dic.items()))
# print(dic_item)
# print(type(list(dic.items())))
# print(type(dic_item))

a = [1,2,3,4]
print(a[::-1])
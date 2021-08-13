from random import choices , choice

class Person:
    count = 0
    def __init__(self,name):
        self.name = name
        Person.count += 1

class Footballer(Person):
    def __init__(self):
        pass
    def Build_team(self, list):
        self.list = list
        Team = [Person(i) for i in self.list]
        return Team

names = open('names.txt','r',encoding="utf8")
list = names.readlines()
list = list[0].split(sep="-") + list[1].split(sep='-')
LEN = len(list)

L, LA = list, []

for i in range(11):
    ch = choice(L)
    LA.append(ch)
    L.pop(L.index(ch))
LB = L

A, B = Footballer(), Footballer()
A_Squad, B_Squad = A.Build_team(LA) , B.Build_team(LB)

print('A')
for name in A_Squad:
    a = name.name
    a = a.replace(" ","")
    a = a.replace('\n',"")
    print(a)
print('B')
for name in B_Squad:
    b = name.name
    b = b.replace(" ","")
    b = b.replace('\n',"")
    print(b)


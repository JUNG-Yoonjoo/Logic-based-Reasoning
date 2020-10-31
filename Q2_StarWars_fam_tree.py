#!/usr/bin/env python
# coding: utf-8

# In[15]:


from kanren import Relation, facts, run, conde, var, eq

x = var()
y = var()

father = Relation()
mother = Relation()

facts(father, ('The Force', 'Anakin Skywalker'),
 ('Cliegg Lars', 'Owen Lars'),
 ('Anakin Skywalker', 'Leia Organa'),
 ('Anakin Skywalker', 'Luke Skywalker'),
 ('Han Solo', 'Ben Solo'))

facts(mother, ('Shmi Skywalker', 'Anakin Skywalker'),
 ('Shmi Skywalker', 'Owen Lars'),
 ('Padme Amidala', 'Leia Organa'),
 ('Padme Amidala', 'Luke Skywalker'),
 ('Leia Organa', 'Ben Solo'))

resultF = run(1, x, father(x, 'Anakin Skywalker'))
resultM = run(1, x, mother(x, 'Anakin Skywalker'))
print(resultF + resultM)

resultF = run(1, x, father(x, 'Owen Lars'))
resultM = run(1, x, mother(x, 'Owen Lars'))
print(resultF + resultM)

resultF = run(1, x, father(x, 'Leia Organa'))
resultM = run(1, x, mother(x, 'Leia Organa'))
print(resultF + resultM)

resultF = run(1, x, father(x, 'Ben Solo'))
resultM = run(1, x, mother(x, 'Ben Solo'))
print(resultF + resultM)


# In[25]:


def grandfather(x, z):
     y = var()
     return conde((father(x, y), father(y, z)))

def grandmother(x, z):
     y = var()
     return conde((mother(x, y), father(y, z)))

resultgf = run(1, x, grandfather(x, 'Leia Organa'))
resultgc = run(2, x, grandfather('The Force', x))
print(resultgf + resultgc)

resultgm = run(1, x, grandmother(x, 'Luke Skywalker'))
resultgc = run(2, x, grandmother('Shmi Skywalker', x))
print(resultgm + resultgc)


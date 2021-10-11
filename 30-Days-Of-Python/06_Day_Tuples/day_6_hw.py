empty_tuple = ()

sisters = ('Katie', 'Maddie', 'Hannah', 'Yasmin')
brothers = ('Younis', 'Eissa', 'Ibby')

siblings = sisters + brothers
print(siblings)

family = len(siblings)
print(family)

family_members = list(siblings)
family_members.insert(0, 'Helen') 
family_members.insert(1, 'Alastair') 
print(family_members)

parents = list()
parents.insert(0, family_members[0]) 
parents.insert(1, family_members[1]) 
print(parents, siblings)

fruit = ['orange', 'apple', 'pineapple', 'mango']
veg = ['leek', 'broccoli', 'peas', 'carrot']
meat = ['chicken', 'lamb', 'beef']

food = fruit + veg + meat
print(food)

to_eat = list(food)
to_eat.pop(3)
print(to_eat)

del to_eat[0:3]
del to_eat[-3:-1]
print(to_eat)
del to_eat

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

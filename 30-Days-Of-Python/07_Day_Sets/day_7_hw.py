it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add('Twitter')
it_companies.update(['Snapchat', 'TikTok'])
it_companies.remove('IBM')
print(it_companies)

# discard doesnt raise any errors

c = A.union(B)
print(c)

print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))

d = B.union(A)
print(c.symmetric_difference(d))

del c
del d

ages_len = len(age)
list_age = list(age)
list_len = len(list_age)
print(ages_len, list_len)

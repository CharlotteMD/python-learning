count = 0 
while count <= 10: 
    print(count)
    count = count + 1

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers: 
    print(number)

reverse_count = 10
while reverse_count > 0:
    print(reverse_count)
    reverse_count = reverse_count - 1

for number in numbers[::-1]:
    print(number)

number_hash = 1
while number_hash <= 7:
    hash_seq = number_hash
    number_hash = number_hash + 1
    if hash_seq ==1: 
        print('#')
    elif hash_seq ==2: 
        print('##')
    elif hash_seq ==3: 
        print('###')
    elif hash_seq ==4: 
        print('####')
    elif hash_seq ==5: 
        print('#####')
    elif hash_seq ==6: 
        print('######')
    else:
        print('#######')

while number_hash <= 8:
    print('# # # # # # # #')
    number_hash = number_hash + 1

number = 0
while number < 11:
    maths = number * number
    print(f'{number} x {number} = {maths}')
    number = number + 1

tech = ['Python', 'Numpy','Pandas','Django', 'Flask']
for x in tech:
    print(x)

for number in range(2, 100, 2):
    print(number)

count = 0

for number in range(1,101):
    count = count + number

print(f'Sum is: {count}')

evens = 0
for number in range(2, 101, 2):
    evens = evens + number
print(f'Evens total: {evens}')

odds = 0
for number in range(1, 100, 2):
    odds = odds + number

print(f'Odds total: {odds}')

fruits = ['banana', 'orange', 'mango', 'lemon']

for x in fruits[::-1]:
    print(x)


countries = ['England', 'Thailand', 'Germany', 'Spain', 'Switzerland']

for x in countries:
    if 'land' in x:
        print(x)
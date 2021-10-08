first_name = 'Charlotte'
last_name = 'Qazi'
language = 'Python'
formated_string = 'I am %s %s. I love %s' %(first_name, last_name, language)
print(formated_string)

formated_string = 'I am {} {}. I love {}'.format(first_name, last_name, language)
print(formated_string)

ice_cream_flavours = ['Mint', 'Choc', 'Cookie', 'Neopolitan','Raspberry ripple']
ice = ', '.join(ice_cream_flavours)
print(ice.split())
formated_string = 'The following flavours are available: %s' % (ice)
print(formated_string)

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

name = 'charly'
a,b,c,d,e,f = name

print(a)
print(b)
print(c)
print(d)

print(name[0])
print(name[1])
print(name[2])
print(name[3])

print(name[-6])
print(name[-5])
print(name[-4])
print(name[-3])

print(name[0:4]) # starts at index 0 and goes up to index 4 but doesnt include the 4th index

print(name[::-1]) # backwards!

print(name[0:6:2]) # slice

print(name.capitalize())
print(name.title())
print(name.swapcase())

full_name = 'Charlotte Mary Qazi'
print(full_name.count('a'))
print(full_name.count('a', 2, 8)) # start at index 2 and finish before index 8
print(full_name.count('ar'))

nick_name = 'Char\tChar\tM\tQazi'
print(nick_name.endswith('zi'))
print(nick_name.endswith('ies'))
print(nick_name.expandtabs())
print(nick_name.expandtabs(20))

print(full_name.find('ry')) # finds first occurence index
print(full_name.rfind('ar')) # finds last occurence index

print(full_name.replace('Qazi', 'Davies'))


full_set = ['Thirty', 'Days', 'Of', 'Python']
print(' '.join(full_set))

company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
co_list = company.split()
use = co_list[1:3]
new_co = ' '. join(use)
print(new_co)
print(new_co.find('Coding'))
print(company[0])
print(company[-1])
print(company[10])
py_co = company.replace('Coding', 'Python')
print(py_co.replace('All', 'Everyone'))
print(py_co[0:1], py_co[7:8], py_co[11:12])
print(company.find('C'))
print(company.rfind('l'))

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', '))

sentence = 'You cannot end a sentence with because because because is a conjunction'
find_cos = int(sentence.find('because'))
print(find_cos)
print(sentence.rfind('because'))

obj_sentence = sentence.split(' ')

print(obj_sentence)

print('''I am enjoying this challenge.
I just wonder what is next.''')

print('''Name\tAge\tCountry\tCity
Asabeneh\t250\tFinland\tHelsinki''')
from __future__ import annotations

class Triangle(object):
   def __init__(self, height: int, base: int):
      self.height = height
      self.base = base

   def calc_area(self) -> int:
      return 0.5 * self.height * self.base


if __name__ == "__main__":
   t1 = Triangle(10,15)
   t2 = Triangle(20, 35)
   print(t1.calc_area())
   print(t2.calc_area())

   a = 10
   print(a) # 10
   print(id(a))
   a = 20
   print(id(a))
   print(a) # 20


a = 30
h = 5.3
v = a + h
 
base = int(input('Base is : ', ))
height = int(input('Height is : ', ))
area = 0.5 * base * height

print(f"{base}")

print(f"The area of the triangle is {area}")

side_a = int(input('Side a is: ', ))
side_b = int(input('Side b is: ', ))
side_c = int(input('Side c is: ', ))
perimeter = side_a + side_b + side_c

print(f'The perimeter of the triangle is {perimeter}')

base = int(input('Length is : ', ))
height = int(input('Width is : ', ))
new_area = 0.5 * base * height
sq_perimeter = 2 * (base * height)

print(f'The area of the rectangle is {new_area}')
print(f'The perimeter of the rectangle is {sq_perimeter}')

pi = 3.14 
radius = int(input('Radius is: ', ))
circle_area = pi * radius * radius
circumference = 2 * pi * radius

print(f'The area of the circle is {circle_area}')
print(f'The perimeter of the triangle is {circumference}')

point_1_x = 2
point_2_x = 2
point_1_y = 6
point_2_y = 10
slope = point_2_y - point_1_y / point_2_x - point_1_x
print(f'The slope is {slope}')

py = len('Python')
# dra = len('Dragon')
# compare = py != dra
# print(compare)

on_py = 'on' in 'Python'
on_dra = 'on' in 'Dragon'
on_in = on_py == on_dra

print('On in Dragon and Python', on_in)

sentence = 'I hope this course is not full of jargon'
check = 'jargon' in sentence
print(check)

py_float = float(py)
py_str = str(py_float)
print(type(py_str))

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

val = 7 // 3
int_val = int(2.7)
print(val == int_val)

print('10' == 10)

str_val = 9.8
check_int = int(str_val)
# print(check_int)
print(check_int == 10)

hours = int(input('I work (hours): ', ))
rate = float(input('I earn (ph): ', ))
earn = hours * rate
print(f'Your weekly earning is {earn}')

years = int(input('How old are you?: ', ) )
days = years * 365
hours = days * 24
mins = days * 60
secs = mins * 60
print(f'You are {secs} seconds old!')

print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 1)
print('''1 1 1 1
2 2 23 4 5
6 7 7821 33 1''')


def add_two_numbers(num1, num2):
    answer = num1 + num2
    return answer

print(add_two_numbers(29, 67))

def circle_area(r):
    area = 3.14 * r * r
    return area

print(circle_area(5))

total = 0
def add_all_nums(*args):
    total = 0
    for a in args:
        total = total + a
        return total
    return total

print(add_all_nums(2, 53, 565, 2343, 1, 1232, 32))

def convert_c_to_f(c):
    f = (c * 9/5) + 32
    print(f)
    return f

c = int(input("Celcius is: ", ))

convert_c_to_f(c)

list = ['dog', 'cat', 'donkey', 'elephant', 'rabbit']

def capitalize_list(list):
    for each in list: 
        print(each.capitalize())
    
capitalize_list(list)

def evens_odds(n):
    evens = 0
    odds = 0
    for number in range(0, n, 2):
        evens = evens + 1
    for number in range(1, n, 2):
        odds = odds + 1
    print(f'Evens total: {evens} Odds total: {odds}')

evens_odds(100)
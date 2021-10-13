# age = int(input("Enter my age: ", ))

# if age >= 18:
#     print("You are old enough to drive")
# else:
#     years_left = 18 - age
#     print(f"You have {years_left} years till you can drive")

# your_age = int(input("Enter your age: ", ))

# difference = age - your_age
# age_gap = abs(difference)

# if difference == 0:
#     print('We are the same age')
# elif difference < 0:
#     if age_gap == 1:
#         print('You are 1 year older than me')
#     else:
#         print(f'You are {age_gap} years older than me')  
# else:
#     if age_gap == 1:
#         print('I am 1 year older than you')
#     else:
#         print(f'I am {age_gap} years older than you')  

# score = int(input("Enter your score: ", ))

# if score >= 80:
#     print('You got an A')
# elif score > 70:
#     print('You got a B')   
# elif score > 60:
#     print('You got a C')   
# elif score > 50:
#     print('You got a D')   
# else:
#     print('You got an F') 

# month = input("Enter the month: ", )

# if month=='December' or month=='January' or month=='February':
#     print('It is Winter') 
# elif month == 'March' or month=='April' or month=='May':
#     print('It is Spring') 
# elif month == 'June' or month=='July' or month=='August':
#     print('It is Summer') 
# elif month == 'September' or month=='October' or month=='November':
#     print('It is Autumn') 
# else:
#     print('Not sure, try again') 

# fruits = ['banana', 'orange', 'mango', 'lemon']

# user_fruit = input("What's your favourite fruit?: ", )

# if user_fruit in fruits:
#     print('That fruit already exist in the list')
# else:
#     fruits.append(user_fruit)
#     print(fruits)

person={
    'first_name': 'Charlotte',
    'last_name': 'Qazi',
    'age': 250,
    'country': 'UK',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'AWS', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

skills_list = person['skills']

if 'skills' in person:
    length = len(skills_list)
    middle = int(length / 2)
    print(skills_list[2])
    print('Python' in skills_list)

if 'JavaScipt' in skills_list or 'React' in skills_list:
    if 'Python' in skills_list or 'Node' in skills_list:
        print('FS Developer')
    else: 
        print('FE Developer')
elif 'Python' in skills_list or 'Node' in skills_list:
    print('BE Developer')
else:
    print('Not a Developer')

if person['is_marred']:
    print(f'{person["first_name"]} {person["last_name"]} is married and lives in {person["country"]}')

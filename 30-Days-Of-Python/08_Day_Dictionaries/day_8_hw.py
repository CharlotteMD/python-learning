dog = {}
dog = {"name": "Zebedee", "color": "brown", "breed": "spaniel", "age": 13}
print(dog)

student = { "first_name": "Charlotte",
            "last_name": "Qazi", 
            "gender": "f", 
            "age": 30, 
            "married": True, 
            "skills": ["React", "Python", "JavaScript"],
            "address": {
                "country": "UK",
                "city": "London"
            }
}
print(len(student))
print(type(student['skills']))

student['skills'].append("CSS")
student['skills'].append("Styled Components")
print(student['skills'])
print(student.keys())
print(student.values())
print(student.items())
student.popitem()
print(student)
del student

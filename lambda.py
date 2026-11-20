add = lambda x, y: x+y

print(add(2,5))

numbers = [1,2,3,4,5]
doubled = list(map(lambda x: x*2, numbers))
print(doubled)

gte_3 = filter(lambda x: x>=3, numbers)
print(list(gte_3))

students = [
    {"name": "Anna", "age": 22},
    {"name": "Ben", "age": 19},
    {'name': "Clara", "age": 23}
]

students.sort(key=lambda x:x['age'])
print(students)
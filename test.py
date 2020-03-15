from requests import post, get, delete

"""ТЕСТИРОВАНИЕ РАБОТЫ UsersResource"""
# Корректные
print(post('http://127.0.0.1:5000/api/v2/users', json={
    'login': 'sklvb',
    'name': 'Skate',
    'surname': 'Lebovski',
    'age': 21,
    'position': 'minister',
    'speciality': 'manager',
    'address': 'Yandex street, 1',
    'password': '1234'
}).json())
print(get('http://127.0.0.1:5000/api/v2/users/1').json())
# print(delete('http://127.0.0.1:5000/api/v2/users/1').json())
print(get('http://127.0.0.1:5000/api/v2/users').json())

# Некорректные
print(post('http://127.0.0.1:5000/api/v2/users', json={  # Отсутствует обязательный параметр name
    'login': 'galaba',
    'surname': 'Stinson',
    'age': 25,
    'password': '87654321'
}).json())
print(delete('http://127.0.0.1:5000/api/v2/users/999').json())  # Пользователя с таким id не существует
print(get('http://127.0.0.1:5000/api/v2/users/12345').json())  # Пользователя с таким id не существует

"""ТЕСТИРОВАНИЕ РАБОТЫ JobsResource"""
# Корректные
print(post('http://127.0.0.1:5000/api/v2/jobs', json={
    'team_leader': 1,
    'job': 'Making a new station',
    'work_size': 30,
    'collaborators': '2, 3',
    'is_finished': False
}).json())
print(get('http://127.0.0.1:5000/api/v2/jobs/1').json())
print(delete('http://127.0.0.1:5000/api/v2/jobs/1').json())
print(get('http://127.0.0.1:5000/api/v2/jobs').json())

# Некорректные
print(post('http://127.0.0.1:5000/api/v2/jobs', json={  # Пользователся с id = 2 не существует
    'team_leader': 2,
    'job': 'Making a new rocket',
    'work_size': 60,
    'collaborators': '5, 6',
    'is_finished': True
}).json())
print(post('http://127.0.0.1:5000/api/v2/jobs', json={  # Отсутствует обязательный параметр work_size
    'team_leader': 1,
    'job': 'Building main office',
    'collaborators': '3, 4',
    'is_finished': False
}).json())
print(delete('http://127.0.0.1:5000/api/v2/jobs/999').json())  # Работы с таким id не существует
print(get('http://127.0.0.1:5000/api/v2/jobs/12345').json())  # Работы с таким id не существует

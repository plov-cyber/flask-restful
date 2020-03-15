from requests import post, get, delete

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
print(get('http://127.0.0.1:5000/api/v2/users').json())
print(delete('http://127.0.0.1:5000/api/v2/users/1').json())

# Некорректные
print(post('http://127.0.0.1:5000/api/v2/users', json={  # Отсутствует обязательный параметр name
    'login': 'galaba',
    'surname': 'Stinson',
    'age': 25,
    'password': '87654321'
}).json())
print(delete('http://127.0.0.1:5000/api/v2/users/999').json())  # Пользователся с таким id не существует
print(get('http://127.0.0.1:5000/api/v2/users/12345').json())  # Пользователся с таким id не существует

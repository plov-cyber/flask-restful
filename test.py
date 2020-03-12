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
    'passsword': '1234'
}))
print(get('http://127.0.0.1:5000/api/v2/users/1').json())
print(delete('http://127.0.0.1:5000/api/v2/users/1').json())
print(get('http://127.0.0.1:5000/api/v2/users').json())

# Некорректные
print()

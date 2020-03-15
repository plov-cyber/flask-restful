from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('login', required=True)
parser.add_argument('name', required=True)
parser.add_argument('surname', required=True)
parser.add_argument('age', type=int, required=True)
parser.add_argument('position')
parser.add_argument('speciality')
parser.add_argument('address')
parser.add_argument('password', required=True)


import json

with open('server_info.json', mode='rt', encoding='utf-8') as json_file:
    json_data = json.load(json_file)


class FlaskConfig():
    JWT_SECRET_KEY = json_data['production']['SERVER']['JWT_SECRET_KEY']
    HOST = json_data['production']['SERVER']['HOST']
    PORT = json_data['production']['SERVER']['PORT']


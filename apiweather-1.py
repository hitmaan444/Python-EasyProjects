import requests

response = requests.get('https://randomuser.me/api')


gender = response.json()['results'][0]['gender']

title=response.json()['results'][0]['name']['title']

first=response.json()['results'][0]['name']['first']


last=response.json()['results'][0]['name']['last']

age=response.json()['results'][0]['phone']['age']
print(f'{title} {first} {last}')
print(f'age: {age}')

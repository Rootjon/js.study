import requests

response = requests.get('https://jsstudy2021.herokuapp.com/')

print(response)
print(response.url)
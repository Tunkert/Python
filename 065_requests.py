import requests

url = "https://api.openbrewerydb.org/"

response_query = requests.get(url + "/breweries?by_city=denver&per_page=3")

data = response_query.json()

print(data)

barrel_10 = data[0]

print(barrel_10['id'])
print(barrel_10['name'])
print(barrel_10['brewery_type'])
print(barrel_10['street'])

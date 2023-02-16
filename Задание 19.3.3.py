import requests

status='available'
res = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})
print('get status cod:', res.status_code)

res = requests.get( f"https://petstore.swagger.io/v2//store/inventory")
print('get status cod:', res.status_code)

res = requests.post( f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json'},
                     data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})

print('post status cod:',res.status_code)

res = requests.put("https://petstore.swagger.io/v2/pet", data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print('put status cod:', res.status_code)

orderId = '11'
res = requests.delete(f'https://petstore.swagger.io/v2/store/order/{orderId}')
print('delete status cod:', res.status_code)

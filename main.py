import requests

SITE = "https://pixe.la/v1/users"
USERNAME = "mohit98"
TOKEN = "sadakhk2h3nj8nsa"

request_body = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=SITE, json=request_body)
print(response.text)
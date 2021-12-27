import requests

SITE = "https://pixe.la/v1/users"
USERNAME = "mohitrathor"
TOKEN = "sadakhk2h3nj8snsa"

# create user id
request_body = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# create new graph
graph_site = f"{SITE}/{USERNAME}/graphs"
headers = {
    "X-USER-TOKEN": TOKEN
}
graph_request = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "ajisai"
}


response = requests.post(url=graph_site, json=graph_request, headers=headers)
print(response.text)
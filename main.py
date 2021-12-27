import requests
import datetime as date


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
graph_id = "graph1"
headers = {
    "X-USER-TOKEN": TOKEN
}
graph_request = {
    "id": graph_id,
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "ajisai"
}


# post the progress
post_site = f"{SITE}/{USERNAME}/graphs/{graph_id}"

today = date.datetime.now()

post_body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("Number of commits: ")
}

response = requests.post(url=post_site, json=post_body, headers=headers)
print(response.text)
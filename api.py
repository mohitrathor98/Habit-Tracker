import requests
import json
import datetime as date

class Pixela:
    def __init__(self) -> None:
        self.site = "https://pixe.la/v1/users"
        self.username = "mohitrathor"
        self.token = "sadakhk2h3nj8snsa"
        self.graph_id = None
        self.headers = {
            "X-USER-TOKEN": self.token
        }
        today = date.datetime.now()
        self.date_format = today.strftime("%Y%m%d")
        
    def create_user(self, username):
        self.username = username
        request_body = {
            "token": self.token,
            "username": self.username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes"
        }
        
        response = requests.post(url=self.site, json=request_body)
        return response.text
    
    def read_data(self):
        
        try:
            with open("graph_data.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
    
    def dump_data(self, graph_id, graph_name):
        
        data = self.read_data()
        if self.username in data.keys():
            data[self.username][graph_id] = graph_name
        else:
            data[self.username] = {}
            data[self.username][graph_id] = graph_name   
            
        with open("graph_data.json", "w") as file:
            json.dump(data, file, indent=4)
        
    
    def create_new_graph(self, graph_id, graph_name, unit, data_type):
        graph_site = f"{self.site}/{self.username}/graphs"
        self.graph_id = graph_id
        graph_requests = {
            "id": self.graph_id,
            "name": graph_name,
            "unit": unit,
            "type": data_type,
            "color": "ajisai"
        }
        
        response = requests.post(url=graph_site, json=graph_requests, headers=self.headers)
        
        if response.status_code == 200:
            self.dump_data(self.graph_id, graph_name)
        return response.text

    def get_graph_id(self, graph_name):
        
        graph_data = self.read_data()
        self.graph_id = None
        
        if self.username not in graph_data.keys():
            return
        
        for key, values in graph_data[self.username].items():
            if values == graph_name:
                self.graph_id = key
    
    def post_progress(self, graph_name ,quantity):
        
        self.get_graph_id(graph_name)
        if self.graph_id == None:
            return "\nInvalid graph name"

        post_site = f"{self.site}/{self.username}/graphs/{self.graph_id}"
        post_body = {
            "date": self.date_format,
            "quantity": quantity
        }
        
        response = requests.post(url=post_site, json=post_body, headers=self.headers)
        return response.text
    
    def update_progress(self, graph_name, quantity):
        
        self.get_graph_id(graph_name)
        if self.graph_id == None:
            return "\nInvalid graph name"
        
        update_site = f"{self.site}/{self.username}/graphs/{self.graph_id}/{self.date_format}"
        update_body = {
            "quantity": quantity
        }
        
        response = requests.put(url=update_site, json=update_body, headers=self.headers)
        return response.text
    
    def delete_progress(self, graph_name):
        
        self.get_graph_id(graph_name)
        if self.graph_id == None:
            return "\nInvalid graph name"
        
        delete_site = f"{self.site}/{self.username}/graphs/{self.graph_id}/{self.date_format}"
        
        response = requests.delete(url=delete_site, headers=self.headers)
        return response.text
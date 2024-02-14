import requests
import random

from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
# staff
username = input("Enter the username: ")
# micro
password = getpass("Enter the password: ")


auth_response = requests.post(
    auth_endpoint, data={"username": username, "password": password}
)
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    headers = {
        "Authorization": f"Token {token}",
    }
    endpoint = "http://localhost:8000/api/products/"

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())

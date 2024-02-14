import requests
import random


def get_user_input():
    while True:
        try:
            method = int(
                input(
                    "Enter the method (1 for GET, 2 for POST, 3 for GET all products, 4 for 404): "
                )
            )
            if method in [1, 2, 3, 4]:
                return method
            else:
                print("Invalid input. Please enter 1, 2, 3 or 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def make_get_request(endpoint):
    response = requests.get(endpoint)
    print(response.json())


def make_post_request(endpoint, data):
    response = requests.post(endpoint, data)
    print(response.json())


method = get_user_input()

if method == 1:
    endpoint = "http://localhost:8000/api/products/1/"
    make_get_request(endpoint)
elif method == 2:
    endpoint = "http://localhost:8000/api/products/"
    data = {
        "title": "New Product",
        "description": "New Description",
        "price": random.randint(1, 80),
    }
    make_post_request(endpoint, data)
elif method == 3:
    endpoint = "http://localhost:8000/api/products/"
    make_get_request(endpoint)
elif method == 4:
    endpoint = "http://localhost:8000/api/products/600/"
    make_get_request(endpoint)

import requests


def null():
    pass


endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint)  # HTTP GET request
# print(get_response.text)

# endpoint = "https://httpbin.org/"
# This isn't an API endpoint, so it will return HTML

# endpoint = "https://httpbin.org/anything"
# This is an API endpoint, so it will return JSON that can be used by Python

print(get_response.json())


# .text returns =
def returnText():
    {
        "args": {},
        "data": "",
        "files": {},
        "form": {},
        "headers": {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Host": "httpbin.org",
            "User-Agent": "python-requests/2.31.0",
            "X-Amzn-Trace-Id": "Root=1-65cbc932-1941c6565a37dd8d673e2f14",
        },
        "json": null,
        "method": "GET",
        "origin": "186.83.184.55",
        "url": "https://httpbin.org/anything",
    }


# .json() returns =
def returnJson():
    {
        "args": {},
        "data": "",
        "files": {},
        "form": {},
        "headers": {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Host": "httpbin.org",
            "User-Agent": "python-requests/2.31.0",
            "X-Amzn-Trace-Id": "Root=1-65cbc932-1941c6565a37dd8d673e2f14",
        },
        "json": None,
        "method": "GET",
        "origin": "186.83.184.55",
        "url": "https://httpbin.org/anything",
    }

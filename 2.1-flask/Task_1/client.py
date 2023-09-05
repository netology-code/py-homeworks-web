import requests

response = requests.post(
    "http://127.0.0.1:5000/users/",
    json={"name": "user_3", "password": "ekjvhijsdfvijdvi"},
)

print(response.status_code)
print(response.text)


response = requests.patch(
    "http://127.0.0.1:5000/users/8",
    json={"name": "new_name", "password": "ekjvhijsdfvijdvi"},
    headers={"Content-Type": "application/json"},
)
print(response.status_code)
print(response.text)

response = requests.get("http://127.0.0.1:5000/users/8")
print(response.status_code)
print(response.text)


response = requests.delete("http://127.0.0.1:5000/users/3")
print(response.status_code)
print(response.text)
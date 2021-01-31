#!/bin/python3
# %%
import os
os.system('python ../app/upload_demo.py &')

# %%
import requests
API_URL = 'http://127.0.0.1:8000/'
API_KEY = 'i0cgsdYL3hpeOGkoGmA2TxzJ8LbbU1HpbkZo8B3kFG2bRKjx3V'
headers = {'UserAPI-Key': API_KEY}
file_dir="/home/vektor/code/nlp-database/nlp_db/tests/"
file_name="Hamlet.txt"
url_path = f"{API_URL}files/{file_name}"

# %%
def test_post():
    with open(file_name) as fp:
        content = fp.read()
        print(content[:40])
    response = requests.post(url_path, data=content)
    print(f"POST status: {response.status_code}")
    print(response.text[:300])
# %%
def test_get():
    response =requests.get(url_path)    
    print(f"GET status: {response.status_code}")
    print(response.text[:250])

# %%

if __name__ == "__main__":
    test_post()
    test_get()


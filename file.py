from flask import Flask, request, jsonify
import requests
import json
import time

app = Flask(_name_)

def fetch_numbers(url):
    try:
        response = requests.get(url, timeout=0.5)
        if response.status_code == 200:
            data = response.json()
            return data.get("numbers", [])
    except requests.exceptions.RequestException:
        pass
    return []

@app.route('/numbers')
def get_numbers():
    urls = request.args.getlist('url')
    numbers_set = set()

    start_time = time.time()
    for url in urls:
        numbers = fetch_numbers(url)
        numbers_set.update(numbers)

    numbers_list = sorted(list(numbers_set))
    elapsed_time = time.time() - start_time

    return jsonify(numbers=numbers_list, elapsed_time=elapsed_time)

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8008)

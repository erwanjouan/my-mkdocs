#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, request, render_template
import yaml

app = Flask(__name__)


def retrieve_secret_from_file(name):
    with open("secrets/secrets.yml", "r") as file:
        secrets = yaml.safe_load(file)
        return secrets['secrets'][name]


@app.route('/secret', methods=['GET'])
def index():
    args = request.args
    name = args.get('name')
    password = retrieve_secret_from_file(name)
    return render_template('index.html', password=password)


app.run(port=8001, debug=True)

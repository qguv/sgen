#!/usr/bin/env python3

from sgen import generate_startup
from flask import Flask, render_template
app = Flask('sgen')

@app.route('/')
def index():
    return render_template('index.html', text=generate_startup())

app.run(port=80)

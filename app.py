#!/usr/bin/env python3

from flask import Flask, render_template
app = Flask('sgen')

from sgen import domains, past_projects
from random import choice

@app.route('/')
def index():
    return render_template('index.html', text=generate_startup())

app.run(port=80)

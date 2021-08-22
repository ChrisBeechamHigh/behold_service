# app.py
from flask import Flask, redirect, url_for, render_template, request, flash
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # TODO render returned JSON in prettier way
    return render_template('image_poster.html')


if __name__ == '__main__':
    app.run()

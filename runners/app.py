from flask import Flask, request, render_template

import sqlite3

app = flask(__name__)

@app.route("/", methods=["GET","POST"])

def index():
from flask import render_template
from app import app
from app.forms import *
import paramiko
from fabric import Connection
from functions import cmd
connection = Connection(host = "trainee@istl", connect_kwargs = {"password" : "istl2024"})


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/navbar')
def navbar():
    return render_template('navbar.html')

@app.route('/showcow')
def showcow():
    stdout, stderr = cmd("cat cow.txt")
    return render_template('showcow.html', cow2=stdout, title="Show the cow in cat.txt")

@app.route('/fabrictest')
def fabrictest():
    output = connection.run("ls -ld /proc", hide = True).stdout.strip()
    return render_template('fabrictest.html', message=output, title="Test the fabric module")
from flask import render_template, redirect, url_for, flash
from app import app, db
from datetime import datetime
from app.forms import *
import paramiko



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/navbar')
def navbar():
    return render_template('navbar.html')

@app.route('/showcow')
def showcow():
    hostname = "localhost"
    username = "trainee"
    password = "istl2024"

    # Create an SSH client instance
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the server
    client.connect(hostname, port=2222, username=username, password=password)

    # Execute commands on the server
    stdin, stdout, stderr = client.exec_command("cat cow.txt")
    stdin.close()
    output = stdout.read()
    output = output.decode("utf-8")
    # output = output[:(len(output) - 1)]

    # Print the output of the command
    # print(output)

    # Close the SSH connection
    client.close()

    return render_template('showcow.html', cow=output)
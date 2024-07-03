from flask import render_template, redirect, url_for, flash
from app import app, db
from datetime import datetime
from app.forms import *
import paramiko
from fabric import Connection
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
    hostname = "istl"
    username = "trainee"
    password = "istl2024"

    # Create an SSH client instance
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the server
    client.connect(hostname, port=22, username=username, password=password)

    # Execute commands on the server
    stdin, stdout, stderr = client.exec_command("ls -ld /proc")
    stdin.close()
    output = stdout.read()
    output = output.decode("utf-8")
    # output = output[:(len(output) - 1)]

    # Print the output of the command
    # print(output)

    # Close the SSH connection
    client.close()

    return render_template('showcow.html', cow=output)

@app.route('/fabrictest')
def fabrictest():
#    connection = Connection(host = "trainee@istl", connect_kwargs = {"password" : "istl2024"})
    output = connection.run("ls -ld /proc", hide = True).stdout.strip()

    return render_template('fabrictest.html', message=output)
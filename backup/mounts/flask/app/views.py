from flask import render_template, redirect, url_for, flash, request
from app import app
from app.forms import *
import paramiko
from fabric import Connection
from functions import cmd
import time
# connection = Connection(host = "trainee@istl", connect_kwargs = {"password" : "istl2024"})


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def navbar():
    return render_template('about.html')

@app.route('/showcow')
def showcow():
    stdout, stderr = cmd("cat cow.txt")
    return render_template('showcow.html', cow2=stdout, title="Show the cow in cat.txt")

@app.route('/fabrictest')
def fabrictest():
    output = connection.run("ls -ld /proc", hide = True).stdout.strip()
    return render_template('fabrictest.html', message=output, title="Test the fabric module")

@app.route('/exercises/lvl_1', methods=['GET', 'POST'])
def lvl_1():
    if request.method == "POST":
        stdout = cmd("check1.sh")
        return render_template('lvl_1.html', title="Level 1", task=stdout)
    else:
        return render_template('lvl_1.html', title="Level 1")

@app.route('/chapter1')
def ch1():
    return render_template('chapter1.html', title="Chapter 1")

ch1ex1_count = 0
@app.route('/chapter1/ex1', methods=['GET', 'POST'])
def ch1_ex1():
    if request.method == "POST":
        stdout = cmd("ch1_ex1_check", "root")
        global ch1ex1_count
        ch1ex1_count += 1
        if ch1ex1_count > 10:
            ch1ex1_count = 0
        return render_template('ch1_ex1.html', title="Chapter 1, Exercise 1", task=stdout, count=ch1ex1_count)
    else:
        return render_template('ch1_ex1.html', title="Chapter 1, Exercise 1")

ch1ex2_count = 0
@app.route('/chapter1/ex2', methods=['GET', 'POST'])
def ch1_ex2():
    if request.method == "POST":
        stdout = cmd("ch1_ex2_check", "trainee")
        global ch1ex2_count
        ch1ex2_count += 1
        if ch1ex2_count > 10:
            ch1ex2_count = 0
        return render_template('ch1_ex2.html', title="Chapter 1, Exercise 2", task=stdout, count=ch1ex2_count)
    else:
        return render_template('ch1_ex2.html', title="Chapter 1, Exercise 2")

ch1ex3_count = 0
@app.route('/chapter1/ex3', methods=['GET', 'POST'])
def ch1_ex3():
    if request.method == "POST":
        stdout = cmd("ch1_ex3_check", "trainee")
        global ch1ex3_count
        ch1ex3_count += 1
        if ch1ex3_count > 10:
            ch1ex3_count = 0
        return render_template('ch1_ex3.html', title="Chapter 1, Exercise 3", task=stdout, count=ch1ex3_count)
    else:
        return render_template('ch1_ex3.html', title="Chapter 1, Exercise 3")
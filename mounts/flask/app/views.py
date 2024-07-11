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
    return render_template('ch1.html', title="Chapter 1")

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

ch1ex4_count = 0
@app.route('/chapter1/ex4', methods=['GET', 'POST'])
def ch1_ex4():
    if request.method == "POST":
        stdout = cmd("ch1_ex4_check", "trainee")
        global ch1ex4_count
        ch1ex4_count += 1
        if ch1ex4_count > 10:
            ch1ex4_count = 0
        return render_template('ch1_ex4.html', title="Chapter 1, Exercise 4", task=stdout, count=ch1ex4_count)
    else:
        return render_template('ch1_ex4.html', title="Chapter 1, Exercise 4")

ch1ex5_count = 0
@app.route('/chapter1/ex5', methods=['GET', 'POST'])
def ch1_ex5():
    if request.method == "POST":
        stdout = cmd("ch1_ex5_check", "trainee")
        global ch1ex5_count
        ch1ex5_count += 1
        if ch1ex5_count > 10:
            ch1ex5_count = 0
        return render_template('ch1_ex5.html', title="Chapter 1, Exercise 5", task=stdout, count=ch1ex5_count)
    else:
        return render_template('ch1_ex5.html', title="Chapter 1, Exercise 5")

ch1ex6_count = 0
@app.route('/chapter1/ex6', methods=['GET', 'POST'])
def ch1_ex6():
    if request.method == "POST":
        stdout = cmd("ch1_ex6_check", "trainee")
        global ch1ex6_count
        ch1ex6_count += 1
        if ch1ex6_count > 10:
            ch1ex6_count = 0
        return render_template('ch1_ex6.html', title="Chapter 1, Exercise 6", task=stdout, count=ch1ex6_count)
    else:
        return render_template('ch1_ex6.html', title="Chapter 1, Exercise 6")

ch1ex7_count = 0
@app.route('/chapter1/ex7', methods=['GET', 'POST'])
def ch1_ex7():
    if request.method == "POST":
        stdout = cmd("ch1_ex7_check", "trainee")
        global ch1ex7_count
        ch1ex7_count += 1
        if ch1ex7_count > 10:
            ch1ex7_count = 0
        return render_template('ch1_ex7.html', title="Chapter 1, Exercise 7", task=stdout, count=ch1ex7_count)
    else:
        return render_template('ch1_ex7.html', title="Chapter 1, Exercise 7")

ch1ex8_count = 0
@app.route('/chapter1/ex8', methods=['GET', 'POST'])
def ch1_ex8():
    if request.method == "POST":
        stdout = cmd("ch1_ex8_check", "trainee")
        global ch1ex8_count
        ch1ex8_count += 1
        if ch1ex8_count > 10:
            ch1ex8_count = 0
        return render_template('ch1_ex8.html', title="Chapter 1, Exercise 8", task=stdout, count=ch1ex8_count)
    else:
        return render_template('ch1_ex8.html', title="Chapter 1, Exercise 8")

@app.route('/chapter1/complete')
def ch1_complete():
    return render_template('ch1_complete.html', title="Chapter 1 complete")
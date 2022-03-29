# import packages
import os
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response

# set path
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

# creat app object 
app = Flask(__name__, template_folder=tmpl_dir)

# creat database connection
DATABASEURI = "postgresql://mz2840:20224111ab@35.211.155.104/proj1part2"
engine = create_engine(DATABASEURI)

# test database connection
@app.before_request
def before_request():
  try:
    g.conn = engine.connect()
  except:
    print ("uh oh, problem connecting to database")
    import traceback; traceback.print_exc()
    g.conn = None

# test database close
@app.teardown_request
def teardown_request(exception):
  try:
    g.conn.close()
  except Exception as e:
    pass

# web homepage
@app.route('/')
def homepage():
  return render_template("main.html")

# web employee login page
@app.route('/employee_login')
def employee_login():
  return render_template("employee.html")

# web manager login page
@app.route('/manager_login')
def manager_login():
  return render_template("manager.html")

# web supplier login page
@app.route('/supplier_login')
def supplier_login():
  return render_template("supplier.html")

# web store display page
@app.route('/store')
def store():
  return render_template("store.html")

# web emplyee page
@app.route('/employee')
def employee_login_after():
  return render_template("employee_login_after.html")

# web manager page
@app.route('/manager')
def manager_login_after():
  return render_template("manager_login_after.html")

@app.route('/shift_information')
def shift_information():
  return render_template("shift_information.html")

@app.route('/employee_manager_searching')
def employee_manager_searching():
  return render_template("employee_manager_searching.html")

@app.route('/payment_information')
def payment_information():
  return render_template("payment_information.html")

@app.route('/Supplier_list')
def Supplier_list():
  return render_template("Supplier_list.html")

@app.route('/customer_payment_information')
def customer_payment_information():
  return render_template("customer_payment_information.html")

@app.route('/customer_sign_up')
def customer_sign_up():
  return render_template("customer_sign_up.html")

@app.route('/pet')
def pet():
  return render_template("pet.html")

@app.route('/supplier')
def supplier_login_after():
  return render_template("supplier_login_after.html")


    

if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    
    HOST, PORT = host, port
    print ("running on %s:%d" % (HOST, PORT))
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)

  run()
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

@app.route('/store_info')
def store_info():
  return render_template("shop_detail_info.html")


# function realize

# employee search shift information by typing in employee's name
@app.route('/shift_information', methods=['POST'])
def shift_information():
  ssnget = request.form['ssn']
  shift = []
  sql = "SELECT shift FROM employee WHERE ssn = '%s' " % (ssnget)
  cursor = engine.execute(sql)
  for result in cursor:
    shift.append(result["shift"])
  cursor.close()
  if len(shift) == 0:
    shift = "wrong ssn typed, please return and type again"
    return render_template("shift_information.html", shift = shift)
  if len(shift) == 1:
    shift = str(shift[0])
    return render_template("shift_information.html", shift = shift)


# employee search product and insurance information by typing in pid or insurance_id
@app.route('/product_insurance_information', methods=['POST'])
def product_insurance_information():
  idget = request.form['id']
  shift = []
  if len(idget) == 7:
    sql = "SELECT * FROM insurance WHERE insurance_id = '%s' " % (idget)
    cursor = engine.execute(sql)
    for result in cursor:
      shift.append(result)
    cursor.close()
    if len(shift) == 0:
      shift = "wrong insurance id typed, please return and type again"
      return render_template("shift_information.html", shift = shift)
    if len(shift) == 1:
      shift = str(shift[0])
      return render_template("shift_information.html", shift = shift)

  if len(idget) == 3:
    sql = "SELECT * FROM product WHERE pid = '%s' " % (idget)
    cursor = engine.execute(sql)
    for result in cursor:
      shift.append(result)
    cursor.close()
    if len(shift) == 0:
      shift = "wrong product id typed, please return and type again"
      return render_template("shift_information.html", shift = shift)
    if len(shift) == 1:
      shift = str(shift[0])
      return render_template("shift_information.html", shift = shift)


# manager search employee information
@app.route('/employee_searching', methods=['POST'])
def employee_searching():
  ssnget = request.form['ssn']
  shift = []
  sql = "SELECT * FROM employee WHERE ssn = '%s' " % (ssnget)
  cursor = engine.execute(sql)
  for result in cursor:
    shift.append(result)
  cursor.close()
  if len(shift) == 0:
    shift = "wrong ssn typed, please return and type again"
    return render_template("shift_information.html", shift = shift)
  if len(shift) == 1:
    shift = str(shift[0])
    return render_template("shift_information.html", shift = shift)


# manager search payment information
@app.route('/payment_searching', methods=['POST'])
def payment_searching():
  idget = request.form['id']
  shift = []
  sql = "SELECT * FROM payment WHERE payment_id = '%s' " % (idget)
  cursor = engine.execute(sql)
  for result in cursor:
    shift.append(result)
  cursor.close()
  if len(shift) == 0:
    shift = "wrong payment id typed, please return and type again"
    return render_template("shift_information.html", shift = shift)
  if len(shift) == 1:
    shift = str(shift[0])
    return render_template("shift_information.html", shift = shift)


 # manager search supplier information
@app.route('/supplier_searching', methods=['POST'])
def supplier_searching():
  idget = request.form['id']
  shift = []
  sql = "SELECT * FROM supplier WHERE supplier_id = '%s' " % (idget)
  cursor = engine.execute(sql)
  for result in cursor:
    shift.append(result)
  cursor.close()
  if len(shift) == 0:
    shift = "wrong supplier id typed, please return and type again"
    return render_template("shift_information.html", shift = shift)
  if len(shift) == 1:
    shift = str(shift[0])
    return render_template("shift_information.html", shift = shift)


# supplier search shop_list information
@app.route('/shop_list', methods=['POST'])
def shop_list():
  idget = request.form['id']
  shift = []
  sql = "SELECT S.shop_name, S.address, S.zip, S.contact_info, S.rating FROM shop S, shop_supplied SS WHERE S.shop_id = SS.shop_id and SS.supplier_id = '%s' " % (idget)
  cursor = engine.execute(sql)
  for result in cursor:
    shift.append(result)
  cursor.close()
  if len(shift) == 0:
    shift = "wrong supplier id typed, please return and type again"
    return render_template("shift_information.html", shift = shift)
  if len(shift) == 1:
    shift = str(shift[0])
    return render_template("shift_information.html", shift = shift)


# manager/employee query shop information
@app.route('/shop_information', methods=['POST'])
def shop_information():
  addressget = request.form['name']
  sql = "SELECT * FROM shop WHERE address = '%s' " % (addressget)
  cursor = g.conn.execute(sql)
  shift = cursor.fetchall()
  cursor.close()
  if len(shift) == 0:
    shift = "wrong shop address typed, please return and type again"
    return render_template("shift_information.html", shift = shift)
  else:
    return render_template("shift_information.html", shift = shift)


# add new customer information to the database 
@app.route('/customer_info',methods=['POST'])
def customer_info():
  ssn = request.form['ssn']
  name = request.form['name']
  address = request.form["address"]
  email = request.form["email"]
  tele = request.form["tele"]
  g.conn.execute("INSERT INTO Customer VALUES (%s,%s,%s,%s,%s)",(ssn,name,address,email,tele))
  return render_template("pet.html")


# add new pet information to the database 
@app.route('/pet_info',methods=['POST'])
def pet_info():
  name = request.form['name']
  age = request.form["age"]
  customer_ssn = request.form["customer_ssn"]
  cat = request.form["cat"]
  g.conn.execute("INSERT INTO Pet (name,category,age,customer_ssn) VALUES (%s,%s,%s,%s)",(name,cat,age,customer_ssn))
  return render_template("main.html")

# add new payment information to the database
@app.route('/payment_info',methods=['POST'])
def payment_info():
  customer_ssn = request.form["customer_ssn"]
  name = request.form["customer_name"]
  email = request.form["email"]
  address = request.form["address"]
  telephone = request.form["telephone"]
  amount = request.form['amount']
  method = request.form["method"]
  productid = request.form["product_id"]

  g.conn.execute("INSERT INTO customer VALUES (%s,%s,%s,%s,%s)",(customer_ssn,name,address,email,telephone))
  g.conn.execute("INSERT INTO payment (amount,method_way,customer_ssn) VALUES (%s,%s,%s)",(amount,method,customer_ssn))
  g.conn.execute("INSERT INTO customer_buy VALUES (%s,%s)",(customer_ssn,productid))
  return render_template("main.html")



if __name__ == "__main__":
  import click
  app.run(debug = True)
  
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
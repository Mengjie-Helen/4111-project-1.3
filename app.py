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
  cursor = engine.execute("SELECT shift FROM employee WHERE ssn = %s",(ssnget,))
  for result in cursor:
    shift.append(result["shift"])
  cursor.close()
  if len(shift) == 0:
    shift = ["wrong ssn typed, please return and type again"]
    return render_template("shift_information.html", shift = shift)
  if len(shift) == 1:
    shift = [shift[0]]
    return render_template("shift_information.html", shift = shift)


# employee search product and insurance information by typing in pid or insurance_id
@app.route('/product_insurance_information', methods=['POST'])
def product_insurance_information():
  idget = request.form['id']
  shift = []
  if len(idget) == 7:
    cursor = engine.execute("SELECT * FROM insurance WHERE insurance_id = %s ",(idget,))
    for result in cursor:
      shift.append(result)
    cursor.close()
    if len(shift) == 0:
      shift = ["wrong insurance id typed, please return and type again"]
      return render_template("shift_information.html", shift = shift)
    if len(shift) == 1:
      shift = [shift[0][0],shift[0][1],int(shift[0][2])]
      return render_template("shift_information.html", shift = shift)

  if len(idget) == 3:
    cursor = engine.execute("SELECT * FROM product WHERE pid = %s" ,(idget,))
    for result in cursor:
      shift.append(result)
    cursor.close()
    if len(shift) == 0:
      shift = ["wrong product id typed, please return and type again"]
      return render_template("shift_information.html", shift = shift)
    if len(shift) == 1:
      shift = [shift[0][0],shift[0][1],int(shift[0][2])]
      return render_template("shift_information.html", shift = shift)

  else: 
    shift = "wrong id typed, please return and type again"
    return render_template("shift_information.html", shift = shift)


# manager search employee information
@app.route('/employee_searching', methods=['POST'])
def employee_searching():
  ssnget = request.form['ssn']
  shift = []
  cursor = engine.execute("SELECT * FROM employee WHERE ssn = %s " ,(ssnget,))
  for result in cursor:
    shift.append(result)
  cursor.close()
  if len(shift) == 0:
    shift = ["wrong ssn typed, please return and type again"]
    return render_template("shift_information.html", shift = shift)
  if len(shift) == 1:
    shift = [shift[0][0],shift[0][1],shift[0][2],int(shift[0][3]),str(shift[0][4]),shift[0][5]]
    return render_template("shift_information.html", shift = shift)


# manager search payment information
@app.route('/payment_searching', methods=['POST'])
def payment_searching():
  idget = request.form['id']
  shift = []
  cursor = engine.execute("SELECT * FROM payment WHERE payment_id = %s", (idget,))
  for result in cursor:
    shift.append(result)
  cursor.close()
  if len(shift) == 0:
    shift = ["wrong payment id typed, please return and type again"]
    return render_template("shift_information.html", shift = shift)
  if len(shift) == 1:
    shift = [shift[0][0],int(shift[0][1]),shift[0][2],shift[0][3]]
    return render_template("shift_information.html", shift = shift)


 # manager search supplier information
@app.route('/supplier_searching', methods=['POST'])
def supplier_searching():
  idget = request.form['id']
  shift = []
  cursor = engine.execute("SELECT * FROM supplier WHERE supplier_id = %s" , (idget,))
  for result in cursor:
    shift.append(result)
  cursor.close()
  if len(shift) == 0:
    shift = ["wrong supplier id typed, please return and type again"]
    return render_template("shift_information.html", shift = shift)
  if len(shift) == 1:
    shift = [shift[0][0],shift[0][1],shift[0][2],shift[0][3]]
    return render_template("shift_information.html", shift = shift)


# supplier search shop_list information
@app.route('/shop_list', methods=['POST'])
def shop_list():
  idget = request.form['id']
  shift = []
  cursor = engine.execute("SELECT S.shop_name, S.address, S.zip, S.contact_info, S.rating FROM shop S, shop_supplied SS WHERE S.shop_id = SS.shop_id and SS.supplier_id = %s " , (idget,))
  for result in cursor:
    shift.append(result)
  cursor.close()
  if len(shift) == 0:
    shift = ["wrong supplier id typed, please return and type again"]
    return render_template("shift_information.html", shift = shift)
  if len(shift) == 1:
    shift = [shift[0][0],shift[0][1],int(shift[0][2]),int(shift[0][3]),int(shift[0][4])]
    return render_template("shift_information.html", shift = shift)


# manager/employee query shop information
@app.route('/shop_information', methods=['POST'])
def shop_information():
  addressget = request.form['name']
  cursor = g.conn.execute("SELECT S.shop_name, S.address, S.zip, S.contact_info, S.rating, P.pname, P.unit_price FROM shop S, product_sold PS, product P WHERE S.shop_id = PS.shop_id and S.address = %s and PS.pid = P.pid  " , (addressget,))
  shift = []
  all = []
  for result in cursor:
    all.append(result)
  if not all:
    shift = ['wrong shop address typed, please return and type again']
    return render_template("shift_information.html", shift = shift)
  cursor.close()
  shift = [all[0][0],all[0][1],int(all[0][2]),int(all[0][3]),int(all[0][4])]
  for i in range(len(all)):
    shift.append(all[i][5])
  #shift = cursor.fetchall()
  #shift = [shift[0][0],shift[0][1],shift[0][2],int(shift[0][3]),int(shift[0][4]),int(shift[0][5])]
  print(shift)
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
  
  cursor = engine.execute("SELECT name FROM customer WHERE ssn = %s" , (customer_ssn,))
  try:
    cursor.mappings().all()[0]['name']
    print('Customer exists')
  except:
    g.conn.execute("INSERT INTO customer VALUES (%s,%s,%s,%s,%s)",(customer_ssn,name,address,email,telephone))
  g.conn.execute("INSERT INTO payment (amount,method_way,customer_ssn) VALUES (%s,%s,%s)",(amount,method,customer_ssn))
  g.conn.execute("INSERT INTO customer_buy VALUES (%s,%s)",(customer_ssn,productid))
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


@app.route('/employee_login_test',methods=['POST'])
def employee_login_test():
  nameget = request.form['name']
  ssnget = request.form['ssn']
  cursor = engine.execute("SELECT * FROM employee WHERE name = %s AND ssn = %s", (nameget,ssnget))
  try:
    cursor.mappings().all()[0]
    return render_template("employee_login_after.html")
  except:
    shift = ["name and ssn do not match, please return and type again"]
    return render_template("shift_information.html", shift = shift)

@app.route('/manager_login_test',methods=['POST'])
def manager_login_test():
  nameget = request.form['name']
  ssnget = request.form['ssn']
  cursor = engine.execute("SELECT * FROM manager WHERE name = %s AND ssn = %s", (nameget,ssnget))
  try:
    cursor.mappings().all()[0]
    return render_template("manager_login_after.html")
  except:
    shift = ["name and ssn do not match, please return and type again"]
    return render_template("shift_information.html", shift = shift)

@app.route('/supplier_login_test',methods=['POST'])
def supplier_login_test():
  nameget = request.form['name']
  ssnget = request.form['id']
  
  if ssnget=='':
    shift = ["supplier name and supplier id do not match, please return and type again"]
    return render_template("shift_information.html", shift = shift)
  else:
    cursor = engine.execute("SELECT * FROM supplier WHERE supplier_name = %s AND supplier_id = %s", (nameget,ssnget))
    try:
      cursor.mappings().all()[0]
      return render_template("supplier_login_after.html")
    except:
     shift = ["supplier name and supplier id do not match, please return and type again"]
     return render_template("shift_information.html", shift = shift)

    
 




if __name__ == "__main__":
  import click
  app.run(debug = True, port=8111, host='0.0.0.0')

  run()
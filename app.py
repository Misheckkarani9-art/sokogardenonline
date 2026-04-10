# Import flask and its components
from flask import *
import pymysql
import os
from flask_cors import CORS
# cross origin resource sharing

# Create an aplicatioon and give it a name

app = Flask(__name__)
CORS(app)


# Configure the location to where your product images will be saved on your applicqation
app.config["UPLOAD_FOLDER"] = "static/images"

# Beloow is the sign up route
@app.route("/api/signup" ,methods =["POST"])
def signup():
    if request.method =="POST":
        # Extract the differennt details entered in the form
        username =request.form["username"]
        email =request.form["email"]
        password = request.form["password"]
        phone = request.form["phone"]
        # By the use of print function lets print all those details on the upcomming request
        # print(username)
        # print(email)
        # print(password)
        # print(phone)
        connection = pymysql.connect(host ="mysql-karanimisheck22.alwaysdata.net",user ="karanimisheck22",password="modcom1234", database="karanimisheck22_sokogarden")
        # Create a cursor to execute the sql queries
        cursor =connection.cursor()

        # Structure an sql to insert the details received from the form
        # %s stands for a placeholder
        sql="INSERT INTO users(username,email,phone,password) VALUES(%s,%s,%s,%s)"
        #Create a tuple that will hold all the data gotten 
        data = (username,email,phone,password)

        # By use of the cursor exercurte the sql as you replace hthe 
        cursor.execute(sql,data)

        # commit the changes to the database
        connection.commit()


        return jsonify({"message": "user reqistered successfully"})



# Below is the login/signin route
@app.route("/api/signin" ,methods =["POST"])
def signin():
    if request.method=="POST":
        #etract the two details entered on the form
        email = request.form["email"]
        password = request.form["password"]


        #Create /establish cconnection too database
        connection =pymysql.connect(host="mysql-karanimisheck22.alwaysdata.net",user ="karanimisheck22",password="modcom1234", database="karanimisheck22_sokogarden")

           # Create a cursor
        cursor =connection.cursor(pymysql.cursors.DictCursor)

        #Sructure the sql query
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"

        # put the data received from the foorm into a atuple
        data  = (email,password)

        #by the use of the cursor execute the sql 
        cursor.execute(sql,data)
        
        # By the use of the cursor execute the sql
        count =cursor.rowcount
        # If there are records returns it means the password and the email aer wrong
        if count == 0:
            return jsonify({"message":"login failed"})
        else:
            #There ust be a user so we create a vvariable that will hold the details of the users fetched from the database
            user=cursor.fetchone()
            # Return the details too the front end as well as a message
            return jsonify ({"message":"user logged in successfully", "user":user})
        
        
# Beloow is the route for adding products
@app.route("/api/add_product",methods =["POST"])
def Addproducts():
    if request.method=="POST":
        # Extract the data entered from the form
        product_name = request.form["product_name"]
        product_description = request.form["product_description"]
        product_cost = request.form["product_cost"]
        product_category = request.form["product_category"]
        # for the product photo we shall fetch it from files as shown below
        product_photo = request.files["product_photo"]

        # Extract the file name of the product photo
        filename = product_photo.filename
        # by the use of the os (operating system) we acn extract the file path where the image is currently saved
        photo_path = os.path.join(app.config["UPLOAD_FOLDER"],filename)

        # save the product phto image into the new location
        product_photo.save(photo_path)

        # print themm out to test whether you are receiving the details
        print(product_name, product_description,product_cost,product_category, product_photo)
        # Establish connectioon
        connection = pymysql.connect(host ="mysql-karanimisheck22.alwaysdata.net",user="karanimisheck22",password="modcom1234",database="karanimisheck22_sokogarden")

        cursor = connection.cursor()

        # structure the query to insert the product details to the database
        sql= "INSERT INTO product_details(product_name, product_description, product_cost,product_category, product_photo) VALUES (%s, %s, %s, %s, %s)"

        # create a tupple that will hold the data from the whitchare current held onto the different variable declared
        data= ( product_name,product_description,product_cost,product_category,filename)

        # Use the cursor to execute the sql as you replace the placeholders with actual data
        cursor.execute(sql,data)

        # comit the changes to the database
        connection.commit()
        
        
        return jsonify({"message": "product added successfully"})


# 1. Define the route.
# 2. Create a function.
# 3. create a connection to the DB.
# 4. create a cursor()
# 5. Structure the query to fetch all the data from the table "product_details"
# 6. Execute the query.
# 7. Create a variable which shall hold/contain all the products fetched from the database.
# 8. Return the products fetched.

@app.route("/api/get_products")
def get_products():
    # create a connection to the Database
    connection = pymysql.connect(host ="mysql-karanimisheck22.alwaysdata.net",user="karanimisheck22",password="modcom1234",database="karanimisheck22_sokogarden")

    #create a cursor.
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    # Structure the query to fetch all the products from the table 
    sql="SELECT * FROM product_details"
    
    #Execute the query
    cursor.execute(sql)

    #Create a variable that hold the data fetched from the table
    products = cursor.fetchall()


    return jsonify(products)
   
# Mpesa Payment Route/Endpoint 
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth
 
@app.route('/api/mpesa_payment', methods=['POST'])
def mpesa_payment():
    if request.method == 'POST':
        amount = request.form['amount']
        phone = request.form['phone']
        # GENERATING THE ACCESS TOKEN
        # create an account on safaricom daraja
        consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
        consumer_secret = "amFbAoUByPV2rM5A"
 
        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
 
        data = r.json()
        access_token = "Bearer" + ' ' + data['access_token']
 
        #  GETTING THE PASSWORD
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
        business_short_code = "174379"
        data = business_short_code + passkey + timestamp
        encoded = base64.b64encode(data.encode())
        password = encoded.decode('utf-8')
 
        # BODY OR PAYLOAD
        payload = {
            "BusinessShortCode": "174379",
            "Password": "{}".format(password),
            "Timestamp": "{}".format(timestamp),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": "1",  # use 1 when testing
            "PartyA": phone,  # change to your number
            "PartyB": "174379",
            "PhoneNumber": phone,
            "CallBackURL": "https://modcom.co.ke/api/confirmation.php",
            "AccountReference": "account",
            "TransactionDesc": "account"
        }
 
        # POPULAING THE HTTP HEADER
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }
 
        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # C2B URL
 
        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        return jsonify({"message": "Please Complete Payment in Your Phone and we will deliver in minutes"})





# Run the application
# app.run(debug=True)
# Import flask and its components
from flask import *
import pymysql
# Create an aplicatioon and give it a name

app = Flask(__name__)


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
        connection = pymysql.connect(host ="localhost",user ="root",password="", database="sokogardenonline")
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
        connection =pymysql.connect(host="localhost",user ="root",password="", database="sokogardenonline")

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
        
        


     






# Run the application
app.run(debug=True)
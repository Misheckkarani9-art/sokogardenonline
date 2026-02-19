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

        # coommiit the changes to the database
        connection.commit()


        return jsonify({"message": "user reqistered successfully"})











# Run the application
app.run(debug=True)
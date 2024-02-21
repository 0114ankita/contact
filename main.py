from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

#creating a connection with db
connection = sqlite3.connect("contactus.db")
create_table_query = "CREATE TABLE IF NOT EXISTS CONTACT (name TEXT, email TEXT, message TEXT)"
connection.execute(create_table_query)

@app.get('/contactus')
def showpage():
    return render_template('index.html')

@app.post('/contactus')
def handler():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    print(name,email,message)

    with sqlite3.connect('contactus.db') as userdata:
        cursor = userdata.cursor()
        user_info_query = f"INSERT INTO CONTACT VALUES ('{name}', '{email}', '{message}')"
        cursor.execute(user_info_query)
        userdata.commit()
    
    return render_template('index.html', msg = "data added to db")

app.run(debug=True)
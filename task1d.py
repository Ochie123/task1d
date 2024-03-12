from flask import Flask, request
import datetime

app = Flask(__name__)

# Defining the name and student ID
name = "Your Name"
student_id = "Your Student ID"

@app.route('/')
def display_info():
    # Getting current date and time
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Displaying the message
    message = f"Name: {name}<br>Student ID: {student_id}<br>Browser Access Time: {now}"
    
    return message

if __name__ == '__main__':
    app.run(debug=True)

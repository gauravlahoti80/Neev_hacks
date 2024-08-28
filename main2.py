from flask import Flask, render_template, request, redirect, url_for, jsonify
from algorithm import en_message, decr_message
from main import main
from secrets import randbelow, choice
# Initialize Flask app with the correct template folder
app = Flask(__name__, template_folder="./templates", static_folder="./static")

# Route for the login page
@app.route('/')
def index():
    return render_template('login.html')

# Route for the signup page
@app.route('/signup')
def signup_page():
    return render_template('signup.html')

# Route to fetch updated messages
@app.route('/fetch_messages')
def fetch_messages():
    messages_list = main() 
    return jsonify(messages_list)

# Route for the dashboard page
@app.route('/dashboard')
def dashboard():
    messages = main()  # Fetch messages using the modified function
    return render_template('dashboard.html', messages_list=messages)

@app.route('/dashboard.html')
def dashboard_template():
    return render_template('dashboard.html')

# Route to handle login form submission
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('userName')  # Fetch username
    password = request.form.get('password')  # Fetch password
    # Simple login validation
    if username == 'admin' and password == 'admin123':
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html')

# Route to handle signup form submission
@app.route('/signup', methods=['POST'])
def signup():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    gmail_id = request.form.get('gmail_id')
    password = request.form.get('pwd')
    print(fname, lname, gmail_id, password)  # Example output, change as needed
    return redirect(url_for('index'))  # Redirect to login after signup

@app.route('/send_mail', methods=['POST'])
def send_mail():
    to = request.form.get('to')
    subject = request.form.get('subject')
    body = request.form.get('body')
    global subject_encrypt, body_encrypt
    subject_encrypt = en_message(subject)
    body_encrypt = en_message(body)
    
    return render_template('dashboard.html')

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    
    
    


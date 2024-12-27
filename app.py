from flask import Flask, render_template, request, redirect, flash, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash

# Flask app setup
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulated data storage
users = {}  # A dictionary to store user information
insurance_forms = []  # A list to store submitted forms

# Home route
@app.route('/')
def home():
    return redirect('/signup')

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        password = request.form['password']

        if email in users:
            flash("Email already registered. Please log in.", "error")
            return redirect('/login')

        hashed_password = generate_password_hash(password)
        users[email] = {
            "first_name": first_name,
            "last_name": last_name,
            "password": hashed_password
        }
        flash("Signup successful! Please log in.", "success")
        return redirect('/login')

    return render_template('signup-btn.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = users.get(email)
        if user and check_password_hash(user['password'], password):
            session['user_id'] = email
            flash("Login successful!", "success")
            return redirect('/form-filling')
        else:
            flash("Invalid email or password.", "error")
            return redirect('/login')

    return render_template('login-btn.html')

# Form-filling route
@app.route('/form-filling', methods=['GET', 'POST'])
def form_filling():
    if 'user_id' not in session:
        flash("Please log in to access the form.", "warning")
        return redirect('/login')

    if request.method == 'POST':
        form_data = {
            "first_name": request.form['firstName'],
            "middle_name": request.form.get('middleName', ''),
            "last_name": request.form['lastName'],
            "gender": request.form['gender'],
            "age": int(request.form['age']),
            "status": request.form['status'],
            "dob": request.form['dob'],
            "street_address": request.form['streetAddress'],
            "city": request.form['city'],
            "state_province": request.form['stateProvince'],
            "zip_code": request.form['zipCode'],
            "email": request.form['email'],
            "phone_number": request.form['phoneNumber'],
            "applicant_type": request.form['applicantType'],
            "applicant_full_name": request.form.get('applicantFullName', ''),
            "applicant_gender": request.form.get('applicantGender', ''),
            "applicant_dob": request.form.get('applicantDob', None)
        }
        insurance_forms.append(form_data)
        flash("Form submitted successfully!", "success")
        return redirect('/form-filling')

    return render_template('index.html')

# Logout route
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect('/login')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

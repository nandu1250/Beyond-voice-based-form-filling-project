from flask import Flask, request, redirect, flash, render_template, session, url_for
import os
import io
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from googletrans import Translator

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session and flash messages

# Initialize the Translator
translator = Translator()

# In-memory user data store (for testing purposes)
users = {}

# Valid ENUM values
VALID_GENDER_VALUES = ['Male', 'Female', 'Other']
VALID_STATUS_VALUES = ['Single', 'Married', 'Student', 'Employed', 'Other']
VALID_APPLICANT_TYPE_VALUES = ['Partner', 'Child', 'Single', 'Married', 'Divorced', 'Widowed', 'Other']

# Home Route
@app.route('/')
def home():
    return render_template('home.html')

# Signup Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Validation
        if not email or not password or not confirm_password:
            flash("All fields are required.", "danger")
            return redirect(url_for('signup'))

        if password != confirm_password:
            flash("Passwords do not match.", "danger")
            return redirect(url_for('signup'))

        if email in users:
            flash("Email already registered. Please log in.", "warning")
            return redirect(url_for('login'))

        # Register the user
        users[email] = {"password": password}
        flash("Signup successful! Please log in.", "success")
        return redirect(url_for('login'))

    return render_template('signup.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Validate user credentials
        user = users.get(email)
        if user and user["password"] == password:
            session['user_id'] = email
            flash("Login successful!", "success")
            return redirect(url_for('index'))
        else:
            flash("Invalid email or password.", "danger")
            return redirect(url_for('login'))

    return render_template('login.html')

# Index Route - Policy Form
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.form['firstName']
        middle_name = request.form.get('middleName', '')
        last_name = request.form['lastName']
        gender = request.form['gender'].strip()  # Strip any leading/trailing spaces
        age = int(request.form['age'])
        status = request.form['status'].strip()  # Same for status
        dob = request.form['dob']
        street_address = request.form['streetAddress']
        city = request.form['city']
        state_province = request.form['stateProvince']
        zip_code = request.form['zipCode']
        email = request.form['email']
        phone_number = request.form['phoneNumber']
        applicant_type = request.form['applicantType'].strip()  # Same for applicant type
        applicant_full_name = request.form.get('applicantFullName', '')
        applicant_gender = request.form.get('applicantGender', '')
        applicant_dob = request.form.get('applicantDob', None)
        digital_signature = request.files.get('digitalSignature')
        signature_data = digital_signature.read() if digital_signature else None

        # Enum value validations
        print(f"Gender: {gender}, Status: {status}, Applicant Type: {applicant_type}")  # Debugging print

        if gender not in VALID_GENDER_VALUES:
            flash("Invalid gender value. Please select from Male, Female, or Other.", "danger")
            return redirect(url_for('index'))

        if status not in VALID_STATUS_VALUES:
            flash("Invalid status value. Please select from Single, Married, Student, Employed, or Other.", "danger")
            return redirect(url_for('index'))

        if applicant_type not in VALID_APPLICANT_TYPE_VALUES:
            flash("Invalid applicant type value. Please select a valid applicant type.", "danger")
            return redirect(url_for('index'))

        # If all validations pass, proceed with the form processing (e.g., storing data, generating PDF, etc.)
        # You can proceed with your logic, such as saving the data, or generating a PDF

    return render_template('index.html')

# Thank You Route
@app.route('/last')
def last():
    return render_template('last.html')

# Logout Route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

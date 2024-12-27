const translations = {
    en: {
        "Medical Insurance Form": "Medical Insurance Form",
        "Language": "Language",
        "Personal Information": "Personal Information",
        "Contact Information": "Contact Information",
        "Other Applicants": "Other Applicants",
        "Submit": "Submit",
        "First Name": "First Name",
        "Middle Name": "Middle Name",
        "Last Name": "Last Name",
        "Gender": "Gender",
        "Age": "Age",
        "Status": "Status",
        "Date of Birth": "Date of Birth",
        "Street Address": "Street Address",
        "City": "City",
        "State/Province": "State/Province",
        "Postal/Zip Code": "Postal/Zip Code",
        "Email": "Email",
        "Phone Number": "Phone Number",
        "Applicant Type": "Applicant Type",
        "Full Name": "Full Name",
        "Digital Signature": "Digital Signature"
    },
    hi: {
        "Medical Insurance Form": "चिकित्सा बीमा फॉर्म",
        "Language": "भाषा",
        "Personal Information": "व्यक्तिगत जानकारी",
        "Contact Information": "संपर्क जानकारी",
        "Other Applicants": "अन्य आवेदक",
        "Submit": "जमा करें",
        "First Name": "पहला नाम",
        "Middle Name": "मध्य नाम",
        "Last Name": "अंतिम नाम",
        "Gender": "लिंग",
        "Age": "आयु",
        "Status": "स्थिति",
        "Date of Birth": "जन्म तिथि",
        "Street Address": "सड़क का पता",
        "City": "शहर",
        "State/Province": "राज्य/प्रांत",
        "Postal/Zip Code": "डाक/पिन कोड",
        "Email": "ईमेल",
        "Phone Number": "फ़ोन नंबर",
        "Applicant Type": "आवेदक प्रकार",
        "Full Name": "पूरा नाम",
        "Digital Signature": "डिजिटल हस्ताक्षर"
    }
};

// Function to change language
function changeLanguage() {
    const selectedLanguage = document.getElementById("languageSelect").value;
    const translation = translations[selectedLanguage];

    // Update text for all elements
    document.getElementById("formTitle").innerText = translation["Medical Insurance Form"];
    document.getElementById("languageLabel").innerText = translation["Language"];
    document.getElementById("personalInfoTitle").innerText = translation["Personal Information"];
    document.getElementById("contactInfoTitle").innerText = translation["Contact Information"];
    document.getElementById("otherApplicantsTitle").innerText = translation["Other Applicants"];
    document.getElementById("submitButton").innerText = translation["Submit"];

    // Update all label texts
    document.getElementById("firstNameLabel").innerText = translation["First Name"];
    document.getElementById("middleNameLabel").innerText = translation["Middle Name"];
    document.getElementById("lastNameLabel").innerText = translation["Last Name"];
    document.getElementById("genderLabel").innerText = translation["Gender"];
    document.getElementById("ageLabel").innerText = translation["Age"];
    document.getElementById("statusLabel").innerText = translation["Status"];
    document.getElementById("dobLabel").innerText = translation["Date of Birth"];
    document.getElementById("streetAddressLabel").innerText = translation["Street Address"];
    document.getElementById("cityLabel").innerText = translation["City"];
    document.getElementById("stateProvinceLabel").innerText = translation["State/Province"];
    document.getElementById("zipCodeLabel").innerText = translation["Postal/Zip Code"];
    document.getElementById("emailLabel").innerText = translation["Email"];
    document.getElementById("phoneNumberLabel").innerText = translation["Phone Number"];
    document.getElementById("applicantTypeLabel").innerText = translation["Applicant Type"];
    document.getElementById("applicantFullNameLabel").innerText = translation["Full Name"];
    document.getElementById("digitalSignatureLabel").innerText = translation["Digital Signature"];
}



// Array of names to cycle through
const names = ["Employee’s", "Manager’s", "Director’s", "Customer's", "Leader’s"];
let currentIndex = 0;
const dynamicTextElement = document.getElementById("dynamic-text");

// Function to update the text with a transition
function changeText() {
    // Fade out effect
    dynamicTextElement.style.opacity = 0;

    setTimeout(() => {
        // Change the text to the next item in the array
        currentIndex = (currentIndex + 1) % names.length; // Loop back to the start
        dynamicTextElement.textContent = names[currentIndex];

        // Fade in effect
        dynamicTextElement.style.opacity = 1;
    }, 500); // Wait 500ms before changing the text
}

// Call the changeText function every 3 seconds
setInterval(changeText, 3000);





const canvas = document.getElementById('signatureCanvas');
const ctx = canvas.getContext('2d');
let isDrawing = false;

canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', stopDrawing);
canvas.addEventListener('mouseout', stopDrawing);

document.getElementById('clearSignature').addEventListener('click', clearSignature);

function startDrawing(event) {
    isDrawing = true;
    ctx.beginPath();
    ctx.moveTo(event.offsetX, event.offsetY);
}

function draw(event) {
    if (isDrawing) {
        ctx.lineTo(event.offsetX, event.offsetY);
        ctx.stroke();
    }
}

function stopDrawing() {
    isDrawing = false;
    ctx.closePath();
}

function clearSignature() {
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas
}







function openSignup() {
    // Fetch the content of signup-btn.html and load it into the container
    fetch('signup-btn.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('signup-container').innerHTML = data;
        })
        .catch(error => {
            console.error('Error loading the signup page:', error);
        });
}




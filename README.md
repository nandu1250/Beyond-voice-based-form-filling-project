# Beyond-QWERTY:Form-Filling Project

[Click Here For Live Demo]([(https://beyond-voice-based-form-filling-project-1.onrender.com))

## Note:
It may take time to go live for the first try in this service, If the server is inactive it go to sleep, When a new request comes in the service its takes a few seconds to wake up(cold start) or it may shows the **502 (Bad Gateway error)** in this issue it may take few minutes so you can try after some time.

This project is deployed using **Render** and utilizes **PostgreSQL** as the cloud database to store and manage data. You can view the live version of the application by clicking the link above.

## Demo Video:
[Watch the Demo Video](<https://drive.google.com/file/d/1ugRQXE77-BNlWGcPVRsDmyfG4aI3MJGq/view?usp=drive_link>)


## Technologies Used:
- **Backend:** Flask
- **Database:** PostgreSQL (Hosted on Render)
- **Deployment:** Render (Cloud Platform)
- **Frontend:** [HTML, CSS, JavaScript]
  
## Features

### 1. Voice Form Filling  
- Implemented a *voice-based form-filling system* using the Web Speech API.  
- Users can fill out forms by speaking into their device's microphone.  
- Enhanced accessibility and usability for individuals with disabilities or limited typing skills.  

### 2. Text-to-Speech Integration
- Implemented a Speech Synthesis feature.
- Reads out form questions when users click on a speaker icon.
- Enhances accessibility and improves user interaction.

### 3. PDF Generation
- Integrated a feature that allows automatic generation of a PDF once the form is completed using voice input.
- Ensures better accessibility and usability for users by providing a downloadable and shareable format.

### 4. PostgreSQL Integration with Cloud Service
- Upgraded the database to PostgreSQL, now deployed on a reliable cloud service.
- Ensures:
  - Improved scalability
  - Enhanced performance
  - Greater data integrity

## Project Overview:
This project is designed to simplifies form filling by using voice commands, enabling seamless and efficient data entry. Users can interact with the system through speech, which is processed and converted into text to populate form fields automatically. The backend is built using Flask and connects to a PostgreSQL database hosted on Render for seamless data management.

## How to Access:
1. Visit the live demo at [Live Demo](<https://mediform.onrender.com>).
2. The application is fully functional and will interact with the PostgreSQL database hosted on Render.

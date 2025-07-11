# 🌦️ Weather Dashboard App

This project is a *Flask-based Weather Dashboard* that fetches *real-time weather data* using the *OpenWeather API, sends weather alerts via **Twilio SMS, and optionally displays location images using the **Google Custom Search API*.  
It is *containerized with Docker* and supports deployment on platforms like *GitHub* and *Render*.

---

## 🚀 Features

- 🌐 Get real-time weather by city name
- 📩 Receive SMS alerts using Twilio
- 🖼️ Display images using Google Custom Search
- 🐳 Run inside Docker container
- 🔐 Secure secrets via `.env` file
- 🧼 Clean deployment using Git & GitHub

---

## 🧰 Technologies Used

| Technology        | Purpose                          |
|------------------|----------------------------------|
| Flask            | Web framework                    |
| OpenWeather API  | Weather data                     |
| Twilio API       | Send SMS alerts                  |
| Google Custom API| Show related city images         |
| Docker           | Containerized deployment         |
| Git & GitHub     | Version control and hosting      |
| Python-dotenv    | Environment variable handling    |

---

## 📂 Project Structure

project_1/
│
├── app.py # Main Flask app
├── requirements.txt # Dependencies
├── Dockerfile # Docker configuration
├── .gitignore # Hides .env & pycache
├── templates/
│ └── index.html # UI template
└── .env # API credentials (not uploaded)


---

## 🔐 .env File Format

> **Note:** `.env` file is ignored from GitHub for security.

TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_PHONE_NUMBER=your_twilio_number
RECIPIENT_PHONE_NUMBER=your_verified_number
OPENWEATHER_API_KEY=your_openweather_key
GOOGLE_API_KEY=your_google_api_key
SEARCH_ENGINE_ID=your_custom_search_id


---

## 🐳 Run the App with Docker

```bash
# Step 1: Build the Docker image
docker build -t weather-dashboard .

# Step 2: Run the container
docker run -p 5000:5000 weather-dashboard

# Step 3: Open the app in your browser
http://localhost:5000

🧪 Run the App Locally (Without Docker)
Step 1: Set up virtual environment

python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On Linux/Mac

Step 2: Install dependencies

pip install -r requirements.txt

Step 3: Create your .env file and fill credentials

Step 4: Run the app

python app.py

💬 Example SMS Alert

Sent via Twilio:

Weather report for Prayagraj:
Temperature: 35°C
Description: Clear sky
Humidity: 48%
Wind Speed: 2.5 m/s
...
(Alert) Hot day! Stay hydrated.

📸 Screenshots

| Web Interface | SMS Alert | Terminal Output |
|---------------|-----------|-----------------|
| ![UI 1](https://github.com/jaiprakashtt/weather-dashboard/blob/main/2025-07-09%20(1).png) | ![SMS](https://github.com/jaiprakashtt/weather-dashboard/blob/main/2025-07-09%20(4).png) | ![Docker](https://github.com/jaiprakashtt/weather-dashboard/blob/main/2025-07-09%20(7).png) |
| ![UI 2](https://github.com/jaiprakashtt/weather-dashboard/blob/main/2025-07-09%20(2).png) | ![Twilio Error Log](https://github.com/jaiprakashtt/weather-dashboard/blob/main/2025-07-09%20(3).png) | — |

---

📝 Useful Commands Used During Development

# Git initialization and push
git init
git remote add origin https://github.com/jaiprakashtt/weather-dashboard.git
git add .
git commit -m "Initial commit"
git push -u origin main

# Secret-safe reset
Remove-Item -Recurse -Force .git
git init
git add .
git commit -m "Removed secrets and added .env support"
git push -u origin main

# Install packages
pip install flask python-dotenv requests twilio

🙋‍♂️ Author
Jai Prakash Tiwari
B.Tech (CSE), United College of Engineering & Research
🔗 GitHub Profile: jaiprakashtt

📢 Disclaimer
This project is for educational/demo purposes only.
Twilio free tier limits SMS/WhatsApp messages.

✅ Project Status: Completed & Ready for Submission


---

### ✅ Next Steps

1. Copy and save this content in your project as `README.md`.
2. Run:

```bash
git add README.md
git commit -m "Final README with full documentation"
git push

## ✅ Final Notes

- Make sure you have added .env to .gitignore
- You can deploy on Render by connecting your GitHub repository
- Twilio free accounts have daily limits — avoid exceeding them

📧 Email: jaiprakasht694@gmail.com
🔗 LinkedIn: linkedin.com/in/jaiprakash-tiwari-2a69992b0
💻 GitHub: github.com/jaiprakashtt
👉 Live Demo URL: https://weather-dashboard-bwse.onrender.com 

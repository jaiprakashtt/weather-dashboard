from flask import Flask, request, render_template, flash, redirect, url_for
import requests
import datetime
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Change this in production

# Twilio credentials
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")
recipient_number = os.getenv("RECIPIENT_PHONE_NUMBER")
client = Client(account_sid, auth_token)

# Home page
@app.route("/")
def index():
    city = "Burundi"
    temp = 25
    description = "Clear sky"
    day = datetime.date.today()
    return render_template('index.html', city=city, temp=temp, description=description, day=day)

# Prediction route
@app.route("/pred", methods=['POST'])
def pred():
    city = request.form.get('city', 'Burundi')

    weather_url = f'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': os.getenv("OPENWEATHER_API_KEY"),
        'units': 'metric'
    }
    data = requests.get(weather_url, params=params).json()

    if 'main' not in data:
        flash("City not found. Try again.", 'error')
        return redirect(url_for('index'))

    try:
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        max_temp = data['main']['temp_max']
        min_temp = data['main']['temp_min']
        pressure = data['main']['pressure']
        precipitation = data.get('rain', {}).get('1h', 0)
        cloudiness = data['clouds']['all']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])

        hot_alert = "(Alert) Hot weather today. Stay hydrated!" if temp >= 40 else ""
        cold_alert = "(Alert) Cold weather today. Wear warm clothes." if temp <= 10 else ""

        report_message = f"""Weather report for {city}:
Temperature: {temp}°C
Description: {description}
Humidity: {humidity}%
Wind Speed: {wind_speed} m/s
Max Temp: {max_temp}°C
Min Temp: {min_temp}°C
Pressure: {pressure} hPa
Precipitation: {precipitation} mm
Cloudiness: {cloudiness}%
Sunrise: {sunrise}
Sunset: {sunset}
{hot_alert}
{cold_alert}
"""

        # Send weather report SMS
        send_report_message(report_message)

    except Exception as e:
        flash(f"Failed to retrieve weather data: {e}", 'error')
        return redirect(url_for('index'))

    # Get image from Google Custom Search
    google_params = {
        'key': os.getenv("GOOGLE_API_KEY"),
        'cx': os.getenv("SEARCH_ENGINE_ID"),
        'q': f"{city} weather",
        'searchType': 'image',
        'imgSize': 'xlarge',
        'num': 1
    }
    google_data = requests.get("https://www.googleapis.com/customsearch/v1", params=google_params).json()
    image_url = google_data.get("items", [{}])[0].get("link", "https://example.com/default_image.jpg")

    day = datetime.date.today()
    return render_template('index.html', city=city, temp=temp, description=description, humidity=humidity,
                           wind_speed=wind_speed, max_temp=max_temp, min_temp=min_temp, pressure=pressure,
                           precipitation=precipitation, cloudiness=cloudiness, sunrise=sunrise, sunset=sunset,
                           hot_alert=hot_alert, cold_alert=cold_alert, day=day, image_url=image_url, icon=icon)

# Function to send SMS
def send_report_message(message):
    try:
        client.messages.create(to=recipient_number, from_=twilio_phone_number, body=message)
        print("✅ SMS sent successfully.")
    except Exception as e:
        print("❌ Failed to send SMS:", e)

# ✅ Corrected render-compatible run command
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

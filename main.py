import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client
import schedule
import time

# send_weather_report = lambda: print("Sending weather report...")

load_dotenv()

def get_weather_report():
    # print("Sending weather report...")
    base_url = "https://api.open-meteo.com/v1/forecast?latitude=-37.814&longitude=144.9633&daily=temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset,precipitation_hours&timezone=Australia%2FSydney&forecast_days=1"
    response = requests.get(base_url)
    data = response.json()
    # print(data["daily"])
    return data

def send_weather_report():
    data = get_weather_report()
    location = [data["latitude"], data["longitude"]]
    temp_max = data["daily"]["temperature_2m_max"][0]
    temp_min = data["daily"]["temperature_2m_min"][0]
    apparent_temp_max = data["daily"]["apparent_temperature_max"][0]
    apparent_temp_min = data["daily"]["apparent_temperature_min"][0]
    sunrise = data["daily"]["sunrise"][0]
    sunset = data["daily"]["sunset"][0]
    precipitation = data["daily"]["precipitation_hours"][0]
    # print(location)

    weather_report = (
        f"Good Morning! Here is your weather report for today:\n"
        f"Lat, Long: {location}\n"
        f"Min and Max temperature: {temp_min}, {temp_max}°C\n"
        f"Feels like: {apparent_temp_min}, {apparent_temp_max}°C\n"
        f"Sunrise: {sunrise}\n"
        f"Sunset: {sunset}\n"
        f"Chance of rain: {precipitation}%\n"
        )
    # print("Sending weather report...")
    send_text_message(weather_report)

def send_text_message(body):
    twilio_sid = os.getenv("TWILIO_ACCOUNT_SID")
    twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")
    recipient_phone_number = os.getenv("RECIPIENT_PHONE_NUMBER")

    client = Client(twilio_sid, twilio_auth_token)

    message = client.messages.create(
        body=body,
        from_=twilio_phone_number,
        to=recipient_phone_number
    )

    print("Text message sent!")


# def main():
#     schedule.every().day.at("10:00").do(send_weather_report)
#     while True:
#         schedule.run_pending()
#         time.sleep(1)

# if __name__ == "__main__":
#     main()

# get_weather_report()
send_weather_report()

import requests
import os


API_KEY = os.environ.get("WEATHER_API")
LAT = -8.05428
LONG = -34.8813
API_CALL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LONG}&appid={API_KEY}"
ONE_CALL = "https://api.openweathermap.org/data/2.5/onecall"
WEATHER_PARAMETERS = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alerts",
    "unit": "metric",
    "lang": "pt_br"
}


def telegram_bot_sendtext(bot_message):
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")

    bot_chat_id = os.environ.get("TELEGRAM_CHAT_ID")

    send_text = \
    f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chat_id}&parse_mode=Markdown&text={bot_message}'

    response_telegram = requests.get(send_text)

    return response_telegram.json()


def will_rain():
    rain = False
    for code in next_12hours:
        if code < 700:
            rain = True

    return rain


response = requests.get(ONE_CALL, params=WEATHER_PARAMETERS)
response.raise_for_status()

data = response.json()

next_12hours = [data["hourly"][i]["weather"][0]["id"] for i in range(0, 11, 1)]

if will_rain():
    telegram_bot_sendtext("Bring a umbrella")
    print("should be rain")
else:
    telegram_bot_sendtext("Well, its gonna be a sunny day")
    print("should be sun")

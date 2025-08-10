from flask import Flask, render_template, request
from weather import get_weather
from db import save_weather, get_all_weather

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form["city"]
        weather_data = get_weather(city)
        if weather_data:
            save_weather(city, weather_data["temp"], weather_data["description"])
    history = get_all_weather()
    return render_template("index.html", weather=weather_data, history=history)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

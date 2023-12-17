from sense_hat import SenseHat
from flask import render_template, Flask

sense = SenseHat()

pitch = sense.get_accelerometer()["pitch"]
roll = sense.get_accelerometer()["roll"]
yaw = sense.get_accelerometer()["yaw"]

app	= Flask(__name__)	

@app.route("/")
def index():
    return render_template("e3.html", pitch=pitch, roll=roll, yaw=yaw)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8085)
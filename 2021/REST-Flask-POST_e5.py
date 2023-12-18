from sense_hat import SenseHat
from flask import render_template, Flask, request

sense = SenseHat()

sense.clear()
sense.set_pixel(0,0,255,0,0)

app	= Flask(__name__)	

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        sense.set_rotation(int(request.form.get("value")))
        print("TEST")
    return render_template("form.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8085)


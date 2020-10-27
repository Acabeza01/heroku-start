from flask import Flask, render_template
from voetbal import haalLijst, ChampionsLeague
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def index():
    land = 'NL'
    Lijst = haalLijst(land)
    datum = datetime.now().replace(second=0, microsecond=0).astimezone(pytz.timezone('Europe/Amsterdam'))
    return render_template("about.html", lijst=Lijst, date=datum, land=land)

@app.route('/eng/')
def eng():
    land='UK'
    Lijst = haalLijst(land) 
    datum = datetime.now().replace(second=0, microsecond=0).astimezone(pytz.timezone('Europe/Amsterdam'))
    return render_template("about.html", lijst=Lijst, date=datum, land=land)

@app.route('/spa/')
def spa():
    land='SP'
    Lijst = haalLijst(land) 
    datum = datetime.now().replace(second=0, microsecond=0).astimezone(pytz.timezone('Europe/Amsterdam'))
    return render_template("about.html", lijst=Lijst, date=datum, land=land)

@app.route('/CL/')
def CL():
    datum = datetime.now().replace(second=0, microsecond=0).astimezone(pytz.timezone('Europe/Amsterdam'))
    return render_template("cl.html", lijst = ChampionsLeague(), date=datum)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

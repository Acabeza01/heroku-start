from flask import Flask, render_template
from voetbal import haalLijst, ChampionsLeague
from datetime import datetime
import pytz

app = Flask('website')

app.config['FREEZER_REMOVE_EXTRA_FILES'] = False
app.config['FREEZER_DESTINATION']= 'docs'

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
# if __name__ == '__main__':
#     from elsa import cli
#     cli(app, base_url='https://acabeza01.github.io')    

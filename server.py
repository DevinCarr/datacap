import json
import datetime
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

TOTAL = 450.0
DATA = {'data': '', 'time': ''}

# Entry point for application
@app.route("/")
def index():
    file = open('data.json', 'r')
    data = json.load(file)
    file.close()
    _monthlyPercentage = "{0:.1f}".format(datetime.date.today().day / 0.30)
    _today = datetime.datetime.today().strftime("%I:%M%p %B %d %Y")
    _date = ''
    if data['time']:
        _date = data['time']
    _percent = ''
    _cap = ''
    if data['data']:
        _percent = ("{0:.1f}").format(float(data['data'])/4.2)
        _cap = ("{0:.1f}").format(float(data['data']))
    return render_template('template.html', date=_date, percent=_percent, cap=_cap, total=TOTAL, today=_today, allowed=_monthlyPercentage)

@app.route("/update")
def update():
    cap = request.args.get('cap')
    if cap:
        data = DATA
        data['data'] = cap
        data['time'] = datetime.datetime.today().strftime("%I:%M%p %B %d %Y")
        with open('data.json', 'w') as file:
            json.dump(data,file)
            return redirect(url_for('index'))
    else:
        return 'Missing data'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)

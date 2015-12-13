import json
import datetime
from flask import Flask, render_template, request
app = Flask(__name__)

TOTAL = 450.0

# Entry point for application
@app.route("/")
def index():
    file = open('data.json', 'r')
    data = json.load(file)
    file.close()
    _monthlyPercentage = "{0:.1f}".format(datetime.date.today().day / 0.30)
    _today = datetime.datetime.today().strftime("%I:%M%p %B %d %Y")
    _date = data['time']
    _percent = ("{0:.1f}").format(float(data['data'])/4.2)
    _cap = ("{0:.1f}").format(float(data['data']))
    return render_template('template.html', date=_date, percent=_percent, cap=_cap, total=TOTAL, today=_today, allowed=_monthlyPercentage)

@app.route("/update", methods=['POST'])
def get():
    if request.method == 'POST':
        req = request.get_json(force=True)
        if req['data'] and req['time']:
            with open('data.json', 'w') as file:
                json.dump(req,file)
                return '200: Successfully updated.'
        else:
            return 'Missing data'
    else:
        return 'Not a POST'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)

from flask import Flask, redirect, url_for, render_template, request
import calendar
from datetime import datetime
import pytz 
app = Flask(__name__)


@app.route('/')
def hello():
        now = datetime.now(pytz.timezone('Africa/Cairo')) # you could pass `timezone` object here
        weekday = now.weekday() 
        x = str(now.strftime("%x"))
        y = x
        return render_template("index.html",nowt = y,daten = x)

    
if __name__ == '__main__':
    app.run(debug= True)
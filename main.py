# -------------------------------------------------------------------
# |                             Title                               |
# -------------------------------------------------------------------
# Dean Ralph
# 2019
#
# Title
# Version
#
# Descripton
# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------

#Imports
from flask import Flask, render_template
import datetime

#Main app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

app.run(debug=True)


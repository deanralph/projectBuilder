# --------------------------------------------------------------------------
# |                             projectBuilder                             |
# --------------------------------------------------------------------------
# Dean Ralph
# 2020-01-09
#
# Project Title: projectBuilder
#
# Short Description:
# A simple python and flask app to create boilerplate for new projects and to
# amend exsisting code to have the correct headers ect...

#Imports
from flask import Flask, render_template

#Create Project
def createProject(proName, shortDesc):
    pass

#Main app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

app.run(debug=True)


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
import pythonHeader
import json

#Reads Config File
def returnConfig(jsonFile):
    with open(jsonFile) as file:
        return file.json.load()

#Create Project
def createProject(proName, shortDesc):
    savePath = f"/mnt/Share/Projects/Python/{proName}"

#Main app
app = Flask(__name__)

@app.route('/')
def pageIndex():
    return render_template("index.html")

@app.route('/settings')
def pageSettings():
    return render_template("settings.html")

app.run(host="0.0.0.0")